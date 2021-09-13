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

		query="""SELECT t1.id, t1.weight#, GROUP_CONCAT(t3.trucks_id) as trucks
        	FROM containers AS t1 
        	JOIN trucks AS t2 
        	ON t1.id = t2.truckid 
        	JOIN sessions as t3 
        	ON t2.truckid = t3.trucks_id 
        	WHERE t3.date BETWEEN  '{0}' AND '{1}'
        	#GROUP BY t3.trucks_id"""
		info = mysql.getData(query.format(in_time, out_time))
		return str(info)

	except:
		print("Error!!!")
	return "i got the item data, ok"
