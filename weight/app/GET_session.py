"""
get session detail.
Author: Shaygs
TODO - when missing element return n/a
"""

from mysql_db import mysql_db
from flask import jsonify
import json

def GET_session(id):
	if id is not None:
		mySQL = mysql_db()

		try:
			session = mySQL.getData(f"SELECT * from sessions WHERE id={id}")

			if len(session) == 0:
				return "Invalid session ID"

			for entry in session:
				if entry['direction']== 'out':
					value = {
						"id": id,
						"truck": entry['trucks_id'],
						"bruto": entry['bruto'],
						"truckTara": (entry['bruto'] - entry['neto']),
						"neto": entry['neto']
					}
				else:
					value = {
						"id": id,
						"truck": entry['trucks_id'],
						"bruto": entry['bruto']
					}
				return json.dumps(value)

		except:
			return "Invalid ID"
	else:
		return "ID missing"