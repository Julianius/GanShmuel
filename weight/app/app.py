from flask import Flask, Response, request
import requests
from GET_health import GET_health
from GET_unknown import GET_unknown
from POST_batch_weight import POST_batch_weight
from GET_session import GET_session

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app - Blue team Weight "

@app.route("/health", methods=['GET'])
def health():
    return GET_health()

@app.route("/unknown", methods=['GET'])
def unknown_weight():
    return GET_unknown()

@app.route("/batch-weight", methods=['POST'])
def batch_weight():
    filename = request.args.get('filename')
    return POST_batch_weight(filename)

@app.route("/weight", methods=['GET']) 
def weight_get_weight(): 
    return "to do"

@app.route("/item/<id>", methods=['GET']) 
def item_weight(id): 
    return "to do"

@app.route("/weight", methods=['POST']) 
def weight_post_weight(): 
    return "to do"

@app.route("/session", methods=['GET']) 
def session_weight(): 
    id = request.args.get('id')
    return GET_session(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)