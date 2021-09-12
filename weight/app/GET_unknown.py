from mysql_db import mysql_db

def GET_unknown():
	mySQL = mysql_db()
 
	try:
		info = mySQL.getData("SELECT distinct id FROM containers WHERE weight IS NULL")		
		if len(info) != 0:
			return '\n'.join(map(str,info))
		return "No missing weights found in data base"
		
	except:		
		return "Weight data is unavailable at the moment."
