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










# myhostname = socket.gethostname()
# myipaddr= socket.gethostbyname(socket.gethostname())

# @app.route('/')
# def index():
#     return render_template('index.html',myhostname=myhostname,myipaddr=myipaddr)


# @app.route('/rates',methods=['GET']
#     with open (nativ shel jason, 'r'):


#     return render_template('rates.html',read jason)


# @app.route('/<roomopen>')
# def roomsesh(roomopen):
#     return render_template('index.html',myhostname=myhostname,myipaddr=myipaddr)

# @app.route('/api/chat/<room>', methods=['GET'])
# def roomread(room):
#     try:
#         with open(f"./chat/chat{room}.txt", "r") as readchat:
#             readchat_is = readchat.read()
#             return  Response(readchat_is , mimetype='text/plain')
#     except:
#         with open(f"./chat/chat{room}.txt", "w") as readchat:
#             return f"Created chat room: {room} "

# @app.route('/api/chat/<room>', methods=['POST'])
# def roomwrite(room):
#     user=request.form['username']
#     msg=request.form["msg"]
#     with open(f"./chat/chat{room}.txt", "a") as chatwrite:
#         chatwrite.write(f"{user}: {msg}")
#         chatwrite.write("\n")
#     return "good job"       

# if __name__ == '__main__':
#     app.run(debug=True, port=9191, host='0.0.0.0')
