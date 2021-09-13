from flask import Flask, request
import os, os.path
import re
from test import check_contacts

app = Flask(__name__)

BRANCHES_ALLOWED = ['main', 'weight-staging', 'billing-staging']
BRANCHES_FORBIDDEN = ['devops', 'weight', 'billing']
REPO = 'https://github.com/Julianius/GanShmuel.git'
PATH = '/GanShmuel/app/'

#@app.before_first_request
#def initial_build():
  #build_app('main', 'billing-staging', '')
  #build_app('main', 'weight-staging', '')
  #build_app('billing-staging', '', '')
  #build_app('weight-staging', '', '')

def committer_report(timestamp, branch_name, merger_name, pusher):
  f = open(PATH + 'commits.txt', 'a')
  text = '[ ' + timestamp + ' ] ' + pusher + ' merged to ' + branch_name + ' from ' + merger_name + '\\n'
  f.write(text)
  f.close()

##TO-DO
##### test(branch_name, pusher)
# CI Hardcoded
# Every 12 hour system sends to team leads what commits were | date | hour | name | description
# Tests - dictionary of all committers
# Logs of CI
# Testing container

def build_app(data):
  timestamp = data.get('head_commit').get('timestamp')
  branch_name = data.get('ref').split('/')[-1]
  merger_name = re.findall(r"'([^']+)'", data.get('head_commit').get('message'))
  if len(merger_name) > 0:
    merger_name = merger_name[0]
  else:
    merger_name = ''
  pusher = data.get('pusher').get('name')
  
  if branch_name in BRANCHES_ALLOWED and merger_name != BRANCHES_FORBIDDEN[0]:

    os.system('rm -rf ' + PATH + 'temp')
    print('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH + 'temp')
    os.system('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH + 'temp')

    check_contacts(branch_name, pusher, merger_name)

    os.system('rm -rf ' + PATH + branch_name)
    os.system('mkdir -p ' + PATH + branch_name)
    os.system('mv '+ PATH + 'temp/* ' + PATH + 'temp/.* ' + PATH + branch_name + '/ 2>/dev/null')
    os.system('rm -rf ' + PATH + 'temp')

    committer_report(timestamp, branch_name, merger_name, pusher)

    if branch_name == BRANCHES_ALLOWED[0]:
      if merger_name == BRANCHES_ALLOWED[1]:
        os.environ["DYNAMIC_PORT"] = "8084"
        os.system('docker-compose -f ' + PATH + branch_name + '/weight/docker-compose.yml -p main-weight up -d --build --force-recreate')
      elif merger_name == BRANCHES_ALLOWED[2]:
        os.environ["DYNAMIC_PORT"] = "8082"
        os.system('docker-compose -f ' + PATH + branch_name + '/billing/Prod/docker-compose.yml -p main-billing up -d --build --force-recreate')
    elif branch_name == BRANCHES_ALLOWED[1]:
      os.environ["DYNAMIC_PORT"] = "8083"
      os.system('docker-compose -f ' + PATH + branch_name + '/weight/docker-compose.yml down  -v ') 
      os.system('docker-compose -f ' + PATH + branch_name + '/weight/docker-compose.yml -p weight-staging up -d --build --force-recreate')
    else:
      os.environ["DYNAMIC_PORT"] = "8081"
      os.system('docker-compose -f ' + PATH + branch_name + '/billing/Prod/docker-compose.yml -p billing-staging up -d --build --force-recreate')

@app.route('/monitor', methods=['GET'])
def home():
    return 'fgfgfg'

@app.route('/health', methods=['GET'])
def health():
    return '200'

@app.route("/myhook", methods=['POST'])
def github_webhook_endpoint():
  build_app(request.get_json())
  return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)