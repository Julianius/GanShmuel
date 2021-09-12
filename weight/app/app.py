from flask import Flask, Response, request
import requests
from GET_health import GET_health
from GET_unknown import GET_unknown

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app - Blue team Weight "

@app.route("/health", methods=['GET'])
def health():
    return GET_health()
    #return Response('<h1>200 OK<h1>')

@app.route("/unknown", methods=['GET'])
def unknown_weight():
    return GET_unknown()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)