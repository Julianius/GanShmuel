"""
TODO Update health - return value
"""
import requests
def test_health():
        req = requests.get("http://localhost:8083/health")
        status_code = req.status_code
        if (status_code < 200 or status_code > 299) and (req.text=='Service item/id : ... ok Service unknown : ... ok Service batch-weight/id : ... ok Service session/id : ... ok '):
                return 1			
        else:
                return 0
def test_unknown():
        req = requests.get("18.157.175.199:8085/unknown")
        status_code = req.status_code
        if (status_code < 200 or status_code > 299) and (req.text!='Weight data is unavailable at the moment.'):
                return 1			
        else:
                return 0
def test_item():
        req = requests.get("18.157.175.199:8085/item/2?from=000000000000")
        status_code = req.status_code
        if (status_code < 200 or status_code > 299) and (req.text!="Weight data is unavailable at the moment."):
                return 1			
        else:
                return 0
def test_batch_weight():
        req = requests.get("18.157.175.199:8085/item/2?from=000000000000")
        status_code = req.status_code
        if (status_code < 200 or status_code > 299) and (req.text!="Weight data is unavailable at the moment."):
                return 1			
        else:
                return 0

def test():
        flag=0
        # flag+=test_home()
        flag+=test_unknown()
        if flag==1:
                return 0
        return 1

if __name__ == '__main__':
    test()