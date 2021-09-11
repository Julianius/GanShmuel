from flask import Flask, request, json
import os, os.path
import subprocess

app = Flask(__name__)

BRANCHES = set(('weight-staging', 'billing-staging', 'main'))
PORTS = { 'devops-production': '8080', 'billing-staging': '8081', 'billing-production': '8082', 'weight-staging': '8083', 'weight-production': '8084' }
REPO = 'https://github.com/Julianius/GanShmuel.git'
#PATHS = { 'local': '/home/julian/GanShmuel/', 'remote': '/home/ec2-user/GanShmuel/' }


@app.route('/health', methods=['GET'])
def health():
    return '200'

@app.route("/myhook", methods=['POST'])
def github_webhook_endpoint():



  # Check the os type to ensure that it is local or remote
  #os_type_cmd='cat /etc/os-release | grep NAME | head -n 1 | cut -d \\" -f 2'
  #OS_TYPE = subprocess.check_output(os_type_cmd, shell=True)
  #print(OS_TYPE)
  #if 'Ubuntu' in str(OS_TYPE):
  #  path = 'local'
  #else:
  #  path = 'remote'  
  #path = PATHS.get(path)
  path = '/GanShmuel/app'
  data = request.get_json()
  branch_name = data.get('ref').split('/')[-1] 

  #os.system('cat /etc/os/release')

  if branch_name in BRANCHES:
    if branch_name == 'main':
      os.system('git clone ' + REPO + ' ' + path + '/temp')
      if os.path.exists(path + 'main-production'):
        os.system('mv '+ path + 'temp/.git ' + path + 'main-production/.git')
      else:
        os.system('mkdir -p ' + path + 'main-production')
        os.system('mv '+ path + 'temp/* ' + path + 'temp/.* ' + path + 'main-production/ 2>/dev/null')
      os.system('rm -rf ' + path + 'temp')
      os.system('docker-compose -f ' + path + 'main-production/billing/docker-compose.yml up -d --force-recreate')
    else:
      print('b')

  return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)