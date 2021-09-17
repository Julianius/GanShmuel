
from GET_session import GET_session
from flask import Flask, Response, request, render_template
from GET_health import GET_health
from GET_unknown import GET_unknown
from GET_weight import GET_weight
from GET_item import GET_item
from POST_batch_weight import POST_batch_weight
from POST_weight import POST_weight


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/ui/health", methods=['GET'])
def uihealth():
    return render_template('ui_health.html')

@app.route("/health", methods=['GET','POST'])
def health():
    return GET_health()

@app.route("/ui/item", methods=['GET']) 
def uiitem(): 
    return render_template('ui_item.html')

@app.route("/item/<id>", methods=['GET','POST'])
def item(id):
    return GET_item(request,id)

@app.route("/ui/unknown", methods=['GET'])
def uiunknown():
    return render_template('ui_unknown.html')

@app.route("/unknown", methods=['GET'])
def unknown():
    return GET_unknown()


@app.route("/ui/batch_weight", methods=['GET'])
def uibatch_weight():
    return render_template('ui_batch_weight.html')

@app.route("/batch_weight/<file>", methods=['POST','GET'])
def batch_weight(file):
    return POST_batch_weight(file)

@app.route("/Pweight", methods=['GET']) 
def pweight():
    return render_template('uiP_weight.html')
@app.route("/Gweight", methods=['GET']) 
def gweight():
    return render_template('uiG_weight.html')

@app.route("/weight", methods=['GET','POST']) 
def weight():
    if request.method =='POST':
       return POST_weight() 
    if request.method == 'GET':
       return GET_weight(request)

@app.route("/ui/session", methods=['GET']) 
def uisession(): 
    return render_template('ui_session.html')

@app.route("/session/<id>", methods=['GET','POST']) 
def session(id): 
    return GET_session(id)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)