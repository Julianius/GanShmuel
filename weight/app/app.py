from flask import Flask, Response, request, render_template
import requests
from GET_health import GET_health
from GET_unknown import GET_unknown
from GET_weight import GET_weight
from GET_item import GET_item
from POST_batch_weight import POST_batch_weight
from GET_session import GET_session

app = Flask(__name__)

@app.route("/")
def home():
    # return "Flask app - Blue team Weight "
    return render_template('Basic.html')

@app.route("/health", methods=['GET'])
def health():
    return GET_health()

@app.route("/unknown", methods=['GET'])
def unknown_weight():
    return GET_unknown()

@app.route("/batch-weight/<file>", methods=['POST','GET'])
def batch_weight(file):
    return POST_batch_weight(file)

@app.route("/item/<id>", methods=['GET']) 
def item_weight(id): 
    return GET_item(id)

# @app.route("/weight", methods=['GET','POST']) 
# def weight_post_weight(): 
#     if request.method == 'POST':
#         return render_template('./UI/GET_weight.html')


@app.route("/weight", methods=['POST']) 
def weight_post_weight(): 
    return POST_weight()

@app.route("/session/<id>", methods=['GET']) 
def session_weight(id): 
    return GET_session(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)