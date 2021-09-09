from flask import Flask, request, json

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return '200'

@app.route("/myhook", methods=['POST'])
def github_webhook_endpoint():

  data = request.get_json()
        
  return str(data.get("repository").get("name"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)