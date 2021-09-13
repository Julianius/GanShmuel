from mysql_db import mysql_db
import datetime

def GET_item(id):
	mysql = mysql_db()

	try:
		enterTime = mysql.getData("SELECT date FROM sessions WHERE trucks_id = id")
		exitTime = mysql.getData("SELECT date FROM sessions WHERE direction = 'out'")
		in_time = enterTime.now().strftime("%Y%m%d%H%M%S")
		out_time = exitTime.now().strftime("%Y%m%d%H%M%S") 
		if(out_time >= in_time):
			duration = (out_time - in_time)
			return duration
		else:
			print("Error time")

	except:
		print("Error!!!")
	return "i got the item data, ok"
