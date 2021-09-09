from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app - Blue Weight Team"


@app.route("/health", methods=['GET'])
def health():
    return Response('<h1>200 OK<h1>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)