import mysql.connector

class mysql_db(object):
	def __init__(self):
		self.db_user = "root"
		self.db_pass = "123456"
		self.db_host = "mysql"
		self.db_name = "db"
		self.connections = None

	def doConnect(self):
		if self.connections is None:
			self.connections = mysql.connector.connect(user='root', password='123456', host='mysql', database='db')
		return self.connections

	def getData(self,querry):
		connected = self.doConnect()
		cur = connected.cursor(dictionary=True, buffered=True)
		cur.execute(querry)
		results = cur.fetchall()
		return results

	def setData(self, query, data):
		connected = self.doConnect()
		cursor = connected.cursor()
		cursor.execute(query, data)
		connected.commit()
  
	def updateData(self, query):
		connected = self.doConnect()
		cursor = connected.cursor()
		cursor.execute(query)
		connected.commit()
