from flask import Flask, Response
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

try:
    mydb = mysql.connector.connect(host='localhost', 
                                   user='root', 
                                   password='123456',
                                   database='db')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


#print(mydb)

@app.route("/")
def home():
    return "Flask app - Blue Weight Team"

@app.route("/health", methods=['GET'])
def health():
    return Response('<h1>200 OK<h1>')

@app.route("/batch-weight", methods=['POST'])
def batch_weight():
    pass

@app.route("/unknown", methods=['GET'])
def unknown():
    pass



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)