from flask import Flask, request
import os, os.path
import re

app = Flask(__name__)

BRANCHES = set(['main', 'weight-staging', 'billing-staging'])
REPO = 'https://github.com/Julianius/GanShmuel.git'
PATH = '/GanShmuel/app/'

def build_app(branch_name, merger_name):
  if branch_name in BRANCHES:
    print(branch_name)
    if branch_name == list(BRANCHES)[0]:
      os.system('git clone ' + REPO + ' ' + PATH + 'temp')
    else:
       os.system('git clone -b ' + branch_name + ' ' + REPO + ' ' + PATH + 'temp')
    
    if os.path.exists(PATH + branch_name):
      os.system('rm -rf ' + PATH + branch_name)
    
    os.system('mkdir -p ' + PATH + branch_name)
    os.system('mv '+ PATH + 'temp/* ' + PATH + 'temp/.* ' + PATH + branch_name + '/ 2>/dev/null')
    os.system('rm -rf ' + PATH + 'temp')

    if branch_name == list(BRANCHES)[0]:
      if merger_name == list(BRANCHES)[1]:
        os.system('docker-compose -f ' + PATH + branch_name + '/weight/docker-compose.yml up -d --force-recreate')
      else:
        os.system('docker-compose -f ' + PATH + branch_name + '/billing/Prod/docker-compose.yml up -d --force-recreate')
    elif branch_name == list(BRANCHES)[1]:
        os.system('docker-compose -f ' + PATH + branch_name + '/weight/docker-compose.yml up -d --force-recreate')
    else:
        os.system('docker-compose -f ' + PATH + branch_name + '/billing/Test/docker-compose.yml up -d --force-recreate')


@app.route('/health', methods=['GET'])
def health():
    return '200'

@app.route("/myhook", methods=['POST'])
def github_webhook_endpoint():
  
  data = request.get_json()
  #print(str(data))
  
  branch_name = data.get('ref').split('/')[-1] 
  merger_name = re.findall(r"'([^']+)'", data.get('head_commit').get('message'))[0]
  build_app(branch_name, merger_name)

  return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
