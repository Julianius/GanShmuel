#Senaty test, check DB is online 
#Author: Shaygs

#from . import app
import requests

def GET_health():
	services = {"unknown"}
	for service in services:
		req = requests.get(f"http://localhost:5000/{service}")
		status_code = req.status_code
		if status_code < 200 or status_code > 299:
			result = f"service {service} : {status_code} server error"
			return result
		else:
			return "200 ok"