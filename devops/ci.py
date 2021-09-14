from flask import Flask, request, render_template
import os, os.path
import re
from test import check_contacts
from monitor.script import script

app = Flask(__name__, template_folder='monitor/templates')

USER = os.environ.get('USER')
BRANCHES_ALLOWED = ['main', 'weight-staging', 'billing-staging']
BRANCHES_FORBIDDEN = ['devops', 'weight', 'billing']
REPO = 'https://github.com/Julianius/GanShmuel.git'
PATH = '/GanShmuel/app/'
DOCKER_COMPOSE_PATHS = { 
  'weight': '/weight/docker-compose.yml',
  'billing': '/billing/Prod/docker-compose.yml'
}
print(str(USER))
APPS_DB_PATHS = {
  #'weight': '/home/' + USER + '/GanShmuel/app/julian-testing/billing/Prod',
  'billing': '/home/' + str(USER) + '/GanShmuel/app/julian-testing/billing/Prod'
}
APPS_PATHS = {
  #'weight': '/home/' + USER + '/GanShmuel/app/julian-testing/billing/Prod',
  'billing': '/home/' + str(USER) + '/GanShmuel/app/julian-testing/billing/Prod'
}


def add_to_committer_report(timestamp, branch_name, merger_branch_name, pusher):
  f = open(PATH + 'commits.txt', 'a')
  text = '[ ' + timestamp + ' ] ' + pusher + ' merged to ' + branch_name + ' from ' + merger_branch_name + '\\n'
  f.write(text)
  f.close()

def run_docker_compose(port, path, path_to_db, path_to_app, name, run_down):
  os.environ["DYNAMIC_PORT"] = port
  os.environ["DYNAMIC_PATH_DB"] = path_to_db
  os.environ["DYNAMIC_PATH_APP"] = path_to_app
  if run_down:
    os.system('docker-compose -f ' + path + ' down  -v ')
  print('docker-compose -f ' + path + ' -p ' + name + ' up -d --force-recreate')
  os.system('docker-compose -f ' + path + ' -p ' + name + ' up -d --force-recreate')

def build_app(data):

  timestamp = data.get('head_commit').get('timestamp')
  branch_name = data.get('ref').split('/')[-1]
  merger_branch_name = re.findall(r"'([^']+)'", data.get('head_commit').get('message'))
  if len(merger_branch_name) > 0:
    merger_branch_name = merger_branch_name[0]
  else:
    merger_branch_name = ''
  pusher = data.get('pusher').get('name')
  
  if branch_name in BRANCHES_ALLOWED and merger_branch_name != BRANCHES_FORBIDDEN[0]:

    os.system('rm -rf ' + PATH + 'temp')
    print('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH + 'temp')
    os.system('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH + 'temp')

    #check_contacts(branch_name, pusher, merger_branch_name)

    os.system('rm -rf ' + PATH + branch_name)
    os.system('mkdir -p ' + PATH + branch_name)
    os.system('mv '+ PATH + 'temp/* ' + PATH + 'temp/.* ' + PATH + branch_name + '/ 2>/dev/null')
    os.system('rm -rf ' + PATH + 'temp')

    add_to_committer_report(timestamp, branch_name, merger_branch_name, pusher)

    if branch_name == BRANCHES_ALLOWED[0]:
      if merger_branch_name == BRANCHES_ALLOWED[1]:
        #run_docker_compose('8084', PATH + branch_name + '/weight/docker-compose.yml', )
        os.environ["DYNAMIC_PORT"] = "8084"
        os.system('docker-compose -f ' + PATH + branch_name + '/weight/docker-compose.yml -p main-weight up -d --force-recreate')
      elif merger_branch_name == BRANCHES_ALLOWED[2]:

        run_docker_compose('8084', PATH + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'billing-main', False)
        #os.environ["DYNAMIC_PORT"] = "8082"
        #os.system('docker-compose -f ' + PATH + branch_name + '/billing/Prod/docker-compose.yml -p main-billing up -d --force-recreate')
    elif branch_name == BRANCHES_ALLOWED[1]:
      os.environ["DYNAMIC_PORT"] = "8083"
      os.system('docker-compose -f ' + PATH + branch_name + '/weight/docker-compose.yml down  -v ') 
      os.system('docker-compose -f ' + PATH + branch_name + '/weight/docker-compose.yml -p weight-staging up -d --force-recreate')
    else:
      #os.environ["DYNAMIC_PORT"] = "8081"
      #os.system('docker-compose -f ' + PATH + branch_name + '/billing/Prod/docker-compose.yml -p billing-staging up -d --force-recreate')
      print(APPS_DB_PATHS['billing'])
      print(APPS_PATHS['billing'])
      run_docker_compose('8084', PATH + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'billing-staging', False)

@app.route('/monitor', methods=['GET'])
def home():
  script()
  return render_template('index.html')

@app.route('/health', methods=['GET'])
def health():
  return '200'

@app.route("/myhook", methods=['POST'])
def github_webhook_endpoint():
  build_app(request.get_json())
  return "OK"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)