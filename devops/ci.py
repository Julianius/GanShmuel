from test import run_tests
from flask import Flask, request, render_template
import os, os.path
import re
from monitor.script import script
from mailing import *
from utils import *

app = Flask(__name__, template_folder='monitor/templates')

DYNAMIC_PATH = str(os.environ.get('DYNAMIC_PATH'))
REPO = 'https://github.com/Julianius/GanShmuel.git'
BRANCHES_ALLOWED = [ 'main', 'weight-staging', 'billing-staging' ]
BRANCHES_FORBIDDEN = [ 'devops', 'weight', 'billing' ]
PATH = '/GanShmuel/app/'
DOCKER_COMPOSE_PATHS = { 
  'weight': '/weight/docker-compose.yml',
  'billing': '/billing/Prod/docker-compose.yml'
}
APPS_DB_PATHS = {
  'weight': DYNAMIC_PATH + 'app/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'app/billing-staging/billing/Prod'
}
APPS_PATHS = {
  'weight': DYNAMIC_PATH + 'app/weight-staging/weight',
  'billing': DYNAMIC_PATH + 'app/billing-staging/billing/Prod'
}

def build_app(data):
  timestamp = data.get('head_commit').get('timestamp')

  branch_name = data.get('ref').split('/')[-1]

  merger_branch_name = re.findall(r"'([^']+)'", data.get('head_commit').get('message'))
  if len(merger_branch_name) > 0:
    merger_branch_name = merger_branch_name[0]
  else:
    merger_branch_name = ''
  pusher = data.get('pusher').get('name')
  #if branch_name ==
  #pusher_email = CONTACT_EMAILS["weight_team"][pusher]

  for team in CONTACT_EMAILS.items():
    if pusher in team[1]:
      if team[0] == "weight_team":
        team_lead_email = CONTACT_EMAILS["weight_team"]['yaelkadosh']
        pusher_email = CONTACT_EMAILS["weight_team"][pusher]
        cur = 'weight-staging'
      elif team[0] == "billing_team":
        team_lead_email = CONTACT_EMAILS["billing_team"]['nadivravivz']
        pusher_email = CONTACT_EMAILS["billing_team"][pusher]
        cur = 'billing-staging'
      else:
        team_lead_email = CONTACT_EMAILS["devops_team"]['matanshk']
        pusher_email = CONTACT_EMAILS["devops_team"][pusher]
      break
  

  if branch_name in BRANCHES_ALLOWED and merger_branch_name != BRANCHES_FORBIDDEN[0]:

    os.system('rm -rf ' + PATH + 'temp')
    print('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH + 'temp')
    os.system('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH + 'temp')
    test_result = 0
    test_result = run_tests(branch_name, merger_branch_name)

    if test_result == 1:
      if cur == 'weight-staging':
        #send_email('Weight team tests failure', 'Some tests have failed please check', team_lead_email, pusher_email)
        pass
      elif cur == 'billing-staging':
        #send_email('Billing team tests failure', 'Some tests have failed please check', team_lead_email, pusher_email)
        pass
      return 1

    os.system('rm -rf ' + PATH + branch_name)
    os.system('mkdir -p ' + PATH + branch_name)
    os.system('mv '+ PATH + 'temp/* ' + PATH + 'temp/.* ' + PATH + branch_name + '/ 2>/dev/null')
    os.system('rm -rf ' + PATH + 'temp')

    add_to_committer_report(PATH, timestamp, branch_name, merger_branch_name, pusher)

    if branch_name == BRANCHES_ALLOWED[0]:
      if merger_branch_name == BRANCHES_ALLOWED[1]:
        run_docker_compose('8084', PATH + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], 'weight-main', False, False)
      elif merger_branch_name == BRANCHES_ALLOWED[2]:
        run_docker_compose('8082', PATH + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'billing-main', False, False)
    elif branch_name == BRANCHES_ALLOWED[1]:
      run_docker_compose('8083', PATH + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], 'weight-staging', False, False)
    else:
      run_docker_compose('8081', PATH + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'billing-staging', False, False)

@app.route('/monitor', methods=['GET'])
def home():
  script()
  return render_template('index.html')

@app.route('/health', methods=['GET'])
def health():
  return '200'

@app.route("/myhook", methods=['POST'])
def github_webhook_endpoint():
  data = request.get_json()
  build_app(data)
  #print(team_lead_email + '   ' + pusher_email)
  return 'OK'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)