from mysql_db import mysql_db

def GET_unknown():
	mySQL = mysql_db()
	try:
		info = mySQL.getData("SELECT distinct id FROM containers WHERE weight IS NULL")

		return info
	except:
		print("DB error")
	return "Weight data is ok"