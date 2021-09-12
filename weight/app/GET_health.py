#Senaty test, check DB is online 
#Author: Shaygs

#from . import app
import requests

def GET_health():
	req = requests.get("http://localhost:8080/unknown")
	if req.status_code < 200 or req.status_code > 299:
		return "200 OKi doki"
	else:
		return "500 internal server error"