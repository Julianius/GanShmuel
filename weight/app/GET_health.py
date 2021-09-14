"""
Check services health
Author: Shaygs
TODO - check POST services
"""

import requests

def GET_health():
<<<<<<< HEAD
	services = {"unknown","batch-weight/id","item/id"}
=======
	services = {"unknown","batch-weight/id","item/id","session/id"}
>>>>>>> 273c5c8cf607147a75f016a148e67b0a5d0cc1cd
	result = ""
	for service in services:
		req = requests.get(f"http://localhost:5000/{service}")
		status_code = req.status_code
		if status_code < 200 or status_code > 299:
			result += f"\n service {service} : ... failed - {status_code} \n"			
		else:
			result += f"\n Service {service} : ... ok \n"
	return result
if __name__ == '__main__':
    GET_health()