from mysql_db import mysql_db

def GET_unknown():
	mySQL = mysql_db()
 
	try:
		info = mySQL.getData("SELECT distinct id FROM containers WHERE weight IS NULL")		
		return '\n'.join(map(str,info))
		
	except Exception as e:	
		print(e)
		return "Weight data is ok"
