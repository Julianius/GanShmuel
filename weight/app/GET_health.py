"""
Check services health
Author: Shaygs
TODO - check POST services
"""

import requests

def GET_health():
	services = {"unknown","batch-weight/id","item/id","session/id","weight"}
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