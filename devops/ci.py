from flask import Flask, request, json
import os

app = Flask(__name__)
branches = set(('weight-staging', 'billing-staging', 'devops-staging', 'main'))
ports = {'devops-production': '8080', 'billing-staging': '8081', 'billing-production': '8082', 'weight-staging': '8083', 'weight-production': '8084'}
repo = 'https://github.com/Julianius/GanShmuel.git'
path = '/home/julian/GanShmuel'

@app.route('/health', methods=['GET'])
def health():
    #os.system('docker run hello-world') 
    return '200'

@app.route("/myhook", methods=['POST'])
def github_webhook_endpoint():
  data = request.get_json()
  branch_name = data.get('ref').split('/')[-1] 
  if branch_name in branches:
    if branch_name == 'main':
      os.system('git clone ' + repo + ' ' + path + '/temp')
      os.system('mv '+ path + '/temp/.git ' + path + 'production/.git')
      os.system('rm -rf ' + path + '/temp')
      #os.system('docker-compose up -f ' + path)
      print('a')
    else:
      print('b')

  return "OK"
###
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)