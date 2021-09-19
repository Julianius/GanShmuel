from flask import Flask, request, render_template
import os, os.path
import re
from test import run_tests
from utils import docker_compose_down, docker_compose_up
from mailing import *
import config

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
        cur = WEIGHT
      elif team[0] == "billing_team":
        team_lead_email = CONTACT_EMAILS["billing_team"]['nadivravivz']
        pusher_email = CONTACT_EMAILS["billing_team"][pusher]
        cur = BILLING
      else:
        team_lead_email = CONTACT_EMAILS["devops_team"]['matanshk']
        pusher_email = CONTACT_EMAILS["devops_team"][pusher]
      break
  

  if branch_name in BRANCHES_ALLOWED and merger_branch_name != BRANCHES_FORBIDDEN[0]:

    os.system('rm -rf ' + PATH_APP + 'temp')
    print('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH_APP + 'temp')
    os.system('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH_APP + 'temp')
    test_result = SUCCESS_CODE
    test_result = run_tests(branch_name, merger_branch_name)

    if test_result == FAILURE_CODE:
      if cur == WEIGHT:
        send_email(WEIGHT + ' ' + HEADING_FAILURE, MESSAGE_FAILURE, team_lead_email, pusher_email)
        pass
      elif cur == BILLING:
        send_email(BILLING + ' ' + HEADING_FAILURE, MESSAGE_FAILURE, team_lead_email, pusher_email)
        pass
      #return 1
    else:
      if cur == WEIGHT:
        send_email(WEIGHT + ' ' + HEADING_SUCCESS, MESSAGE_SUCCESS, team_lead_email, pusher_email)
        pass
      elif cur == BILLING:
        send_email(BILLING + ' ' + HEADING_SUCCESS, MESSAGE_SUCCESS, team_lead_email, pusher_email)
        pass

    os.system('rm -rf ' + PATH_APP + branch_name)
    os.system('mkdir -p ' + PATH_APP + branch_name)
    os.system('mv '+ PATH_APP + 'temp/* ' + PATH_APP + 'temp/.* ' + PATH_APP + branch_name + '/ 2>/dev/null')
    os.system('rm -rf ' + PATH_APP + 'temp')

    add_to_committer_report(timestamp, branch_name, merger_branch_name, pusher)
    try:
      if branch_name == BRANCHES_ALLOWED[0]:
        if merger_branch_name == BRANCHES_ALLOWED[1]:
          config.SWITCHER_MAIN_WEIGHT = 1 - config.SWITCHER_MAIN_WEIGHT
          docker_compose_down(PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['weight'], str(config.SWITCHER_MAIN_WEIGHT) + 'main')
          config.SWITCHER_MAIN_WEIGHT = 1 - config.SWITCHER_MAIN_WEIGHT
          docker_compose_up('8084', PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], str(config.SWITCHER_MAIN_WEIGHT) + 'main', False)
          config.SWITCHER_MAIN_WEIGHT = 1 - config.SWITCHER_MAIN_WEIGHT
        elif merger_branch_name == BRANCHES_ALLOWED[2]:
          config.SWITCHER_MAIN_BILLING = 1 - config.SWITCHER_MAIN_BILLING
          docker_compose_down(PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['billing'], str(config.SWITCHER_MAIN_BILLING) + 'main')
          config.SWITCHER_MAIN_BILLING = 1 - config.SWITCHER_MAIN_BILLING
          docker_compose_up('8082', PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], str(config.SWITCHER_MAIN_BILLING) + 'main', False)
          config.SWITCHER_MAIN_BILLING = 1 - config.SWITCHER_MAIN_BILLING
      elif branch_name == BRANCHES_ALLOWED[1]:
        config.SWITCHER_STAGING_WEIGHT = 1 - config.SWITCHER_STAGING_WEIGHT
        docker_compose_down(PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['weight'], str(config.SWITCHER_STAGING_WEIGHT) + 'staging')
        config.SWITCHER_STAGING_WEIGHT = 1 - config.SWITCHER_STAGING_WEIGHT
        docker_compose_up('8083', PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['weight'], APPS_DB_PATHS['weight'], APPS_PATHS['weight'], str(config.SWITCHER_STAGING_WEIGHT) + 'staging', False)
        config.SWITCHER_STAGING_WEIGHT = 1 - config.SWITCHER_STAGING_WEIGHT
      else:
        config.SWITCHER_STAGING_BILLING = 1 - config.SWITCHER_STAGING_BILLING
        docker_compose_down(PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['billing'], str(config.SWITCHER_STAGING_BILLING) + 'staging')
        config.SWITCHER_STAGING_BILLING = 1 - config.SWITCHER_STAGING_BILLING
        docker_compose_up('8081', PATH_APP + branch_name + DOCKER_COMPOSE_PATHS['billing'], APPS_DB_PATHS['billing'], APPS_PATHS['billing'], str(config.SWITCHER_STAGING_BILLING) + 'staging', False)
        config.SWITCHER_STAGING_BILLING = 1 - config.SWITCHER_STAGING_BILLING
      
      if cur == WEIGHT:
        send_email(WEIGHT + ' ' + HEADING_SUCCESS_DEPLOY, MESSAGE_SUCCESS_DEPLOY, team_lead_email, pusher_email)
        pass
      elif cur == BILLING:
        send_email(BILLING + ' ' + HEADING_SUCCESS_DEPLOY, MESSAGE_SUCCESS_DEPLOY, team_lead_email, pusher_email)
        pass

    except:
      if cur == WEIGHT:
        send_email(WEIGHT + ' ' + HEADING_FAILURE_DEPLOY, MESSAGE_FAILURE_DEPLOY, team_lead_email, pusher_email)
        pass
      elif cur == BILLING:
        send_email(BILLING + ' ' + HEADING_FAILURE_DEPLOY, MESSAGE_FAILURE_DEPLOY, team_lead_email, pusher_email)
        pass

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