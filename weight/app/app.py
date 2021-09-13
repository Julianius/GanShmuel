from POST_batch_weight import POST_batch_weight
from flask import Flask, Response, request
import requests
from GET_health import GET_health
from GET_unknown import GET_unknown
from GET_weight import GET_weight
from GET_item import GET_item

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

@app.route("/weight", methods=['GET'])
def weight_weight():
    # return f"{fromTime} {toTime} {filter}"
    return GET_weight(request)

@app.route("/batch-weight/<file>", methods=['POST', 'GET'])
def batch_weight(file):
    return POST_batch_weight(file)

@app.route("/weight", methods=['GET']) 
def weight_get_weight(): 
    return "to do"

@app.route("/item/<id>", methods=['GET']) 
def item_weight(id): 
    return GET_item(id)

@app.route("/weight", methods=['POST']) 
def weight_post_weight(): 
    return "to do"

@app.route("/session/<id>", methods=['GET']) 
def session_weight(id): 
    return "to do"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)