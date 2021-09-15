from mysql_db import mysql_db
from datetime import datetime
from flask import request
import json

def GET_item(id):
	mysql = mysql_db()

	fromTime = request.args.get('from') if request.args.get('from') else datetime.now().strftime("%Y%m%d000000")
	toTime = request.args.get('to') if request.args.get('to') else datetime.now().strftime("%Y%m%d%H%M%S")
	
	try:
		if id.isdigit():
			query = """SELECT DISTINCT t1.truckid, t1.weight, GROUP_CONCAT(t2.id) as sessions 
					FROM trucks AS t1 
					JOIN sessions as t2 
					ON t1.id = t2.trucks_id
					WHERE t2.date BETWEEN  '{0}' AND '{1}'
					AND t1.id = '{2}'
					GROUP BY t1.id;"""
		
		elif not id.isdigit():
			query = """SELECT DISTINCT t1.id, t1.weight, GROUP_CONCAT(t3.id) as sessions 
					FROM containers AS t1 
					JOIN containers_has_sessions as t2
					ON t1.id = t2.containers_id
					JOIN sessions as t3
					ON t2.sessions_id = t3.id
					WHERE t3.date BETWEEN  '{0}' AND '{1}'
					AND t1.id = '{2}'
					GROUP BY t1.id;"""

		info = mysql.getData(query.format(fromTime, toTime, id))
		if len(info) != 0:	
			value = {
				"id": id,
				"tara": info[0]['weight'],
				"sessions": info[0]['sessions'],
			}
			return json.dumps(value)
		return "No data found"
	
	except:
		return "Weight data is unavailable at the moment."