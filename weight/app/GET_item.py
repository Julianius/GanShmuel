from mysql_db import mysql_db
import datetime
from flask import request

def GET_item(id):
	mysql = mysql_db()
 
	t1 = request.args.get('t1')
	t2 = request.args.get('t2')

	try:
		enterTime = mysql.getData(f"SELECT date FROM sessions WHERE trucks_id = {id}")
		exitTime = mysql.getData("SELECT date FROM sessions WHERE direction = 'out'")
		in_time = enterTime[0]['date']
		out_time = exitTime[0]['date']
		if(out_time >= in_time):
			duration = (out_time - in_time)
			return duration
		
		else:
			print("Error time")

	except:
		print("Error!!!")
	return "i got the item data, ok"
