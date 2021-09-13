import requests
import json

def check(thecheck,therespone):
    if str(thecheck) == str(therespone):
        return 0
    else:
        return 1

def checkhealth():
    urlname=['health','provider','rates','trucks']
    for url in urlname:
        URL = "http://localhost:8081/{}".format(url)
        res = requests.get(url=URL)
        test = check(res.status_code, "200")
        if test==1:
            break
    return test

def checkprovider():
        URL = "http://localhost:8081/api/provider"
        with open(f'testfile/testfile.txt', "r") as testfile:
            readtest=testfile.readlines()
        for line in range(len(readtest)):
            tojson = readtest[line]
            usejson = json.loads(tojson)
            payload = usejson['POST']
            r = requests.post(url=URL, data=payload)
            try:
                r_dict = json.loads(r.text)
                tojson2 = readtest[line].replace('valuetochange', '{0}'.format(r_dict['id']))
            except json.decoder.JSONDecodeError:
                tojson2 = readtest[line]
            usejson2 = json.loads(tojson2)
            testvalue=usejson2['return']
            test = check(str(r.text).replace("\"","\'").replace("\n","").replace("\t","").replace(" ",""), str(testvalue).replace("\"","\'").replace("\n","").replace("\t","").replace(" ",""))
            # test = check(r.status_code, "400")
            if test == 1:
                break
        return test
def main():
    first = checkhealth()
    sectest = checkprovider()
    print(sectest,first)
    if first==0 and sectest==0:
        print("no error found")
        return 0
    else:
        return 1
main()
