from flask import Flask, request, json
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return '200'

@app.route("/myhook", methods=['POST'])
def github_webhook_endpoint():

  data = request.get_json()
  branch_name = data.get("ref").split("/")[-1] 

  os.system('git clone "https://github.com/Julianius/GanShmuel" origin ' + branch_name) 
  return "OK"
#asdasdasd
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)