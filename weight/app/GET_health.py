"""
Check services health
Author: Shaygs
TODO - check POST services
"""

import requests

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

if __name__ == '__main__':
    tast()