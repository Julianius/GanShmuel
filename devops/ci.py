from test import run_tests
from flask import Flask, request, render_template
import os, os.path
import re
from mailing import *
from utils import docker_compose_up
from config import *

app = Flask(__name__, template_folder='monitor/templates')

def add_to_committer_report(timestamp, branch_name, merger_branch_name, pusher):
  f = open(PATH_APP + 'commits.txt', 'a')
  text = '[ ' + timestamp + ' ] ' + pusher + ' merged to ' + branch_name + ' from ' + merger_branch_name + '\n'
  f.write(text)
  f.close()

def build_app(data):
  timestamp = data.get('head_commit').get('timestamp')

  branch_name = data.get('ref').split('/')[-1]

  merger_branch_name = re.findall(r"'([^']+)'", data.get('head_commit').get('message'))
  if len(merger_branch_name) > 0:
    merger_branch_name = merger_branch_name[0]
  else:
    merger_branch_name = ''
  pusher = data.get('pusher').get('name')

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

    os.system('rm -rf ' + PATH_APP + 'temp')
    print('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH_APP + 'temp')
    os.system('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH_APP + 'temp')
    test_result = 0
    test_result = run_tests(branch_name, merger_branch_name)

    if test_result == 1:
      if cur == 'weight-staging':
        #send_email('Weight team tests failure', 'Some tests have failed please check', team_lead_email, pusher_email)
        pass
      elif cur == 'billing-staging':
        #send_email('Billing team tests failure', 'Some tests have failed please check', team_lead_email, pusher_email)
        pass
      #return 1

    os.system('rm -rf ' + PATH_APP + branch_name)
    os.system('mkdir -p ' + PATH_APP + branch_name)
    os.system('mv '+ PATH_APP + 'temp/* ' + PATH_APP + 'temp/.* ' + PATH_APP + branch_name + '/ 2>/dev/null')
    os.system('rm -rf ' + PATH_APP + 'temp')

    add_to_committer_report(timestamp, branch_name, merger_branch_name, pusher)

    if branch_name == BRANCHES_ALLOWED[0]:
      if merger_branch_name == BRANCHES_ALLOWED[1]:
        docker_compose_up('8084', PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], 'weight-main', False)
      elif merger_branch_name == BRANCHES_ALLOWED[2]:
        docker_compose_up('8082', PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'billing-main', False)
    elif branch_name == BRANCHES_ALLOWED[1]:
      docker_compose_up('8083', PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], 'weight-staging', False)
    else:
      docker_compose_up('8081', PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], 'billing-staging', False)

@app.route('/monitor', methods=['GET'])
def home():
  #script()
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