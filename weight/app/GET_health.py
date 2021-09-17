"""
Check services health
Author: Shaygs
TODO - check POST services
"""

import requests

<<<<<<< HEAD
def tastget():
	req = requests.get(f"http://localhost:5000/unknown")
	if req.status_code < 200 or req.status_code > 299:
		return 1
def tast():
	flag+=tastget()
	if flag>8:
		return 1
	else:
		return 0

=======
def GET_health():
	services = {"unknown","batch_weight/file","item/id","session/id"}
	result = ""
	for service in services:
		req = requests.get(f"http://localhost:5000/{service}")
		status_code = req.status_code
		if status_code < 200 or status_code > 299:
			result += f"\n service {service} : ... failed - {status_code} \n"			
		else:
			result += f"\n Service {service} : ... ok \n"
	return result
>>>>>>> 662024b087cea32a48086d2ba4f38066167be4d3
if __name__ == '__main__':
    tast()