from flask import Flask, render_template,request
from flask import Response
import mysql.connector

ifconnect = False
try:
    billingdb = mysql.connector.connect(
    host="billingdb",
    user="root",
    password="1234!",
    )
    mycursor = billingdb.cursor()
    mycursor.execute("select 1")
    myresult = mycursor.fetchall()
    billingdb.commit()
    ifconnect = True
except:
    ifconnect = False


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Billing Blue Site"

@app.route('/health')
def health():
    if ifconnect == True:
        return Response({"Ok"},status=200)
    else:
        return Response({"Internal server error"},status=500)


if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')
