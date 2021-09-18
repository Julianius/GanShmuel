import requests
import json

def check(thecheck, therespone):
    if str(thecheck) == str(therespone):
        return 0
    else:
        return 1


def checkhealth():
    urlname = ['health', 'providers', 'rates', 'trucks']
    for url in urlname:
        URL = "http://localhost:8085/{0}".format(url)
        res = requests.get(url=URL)
        test = check(res.status_code, "200")
        if test == 1:
            break
    return test


def checkprovider():
    URL = "http://localhost:8085/api/providers"
    # provider_id_in_db=[]
    with open(f'testfile/testfile.txt', "r") as testfile:
        readtest = testfile.readlines()
        for line in range(0,1):
            linefromfile = readtest[line]
            jsonfromtext = json.loads(linefromfile)
            payload = jsonfromtext['POST']
            r = requests.post(url=URL, data=payload)
            try:
                r_dict = json.loads(r.text)
                linefromfile = readtest[line].replace('valuetochange', '{}'.format(r_dict['id']))
                provider_id_in_db = r_dict['id']
            except json.decoder.JSONDecodeError:
                linefromfile = readtest[line]
            jsonfromtext2 = json.loads(linefromfile)
            testvalue = jsonfromtext2['return']
            test = check(str(r.text).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""),
                         str(testvalue).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""))
            # test = check(r.status_code, "400")
            if test == 1:
                break
        return test , provider_id_in_db


def checkrates():
    URL = "http://localhost:8085/api/rates"
    with open(f'testfile/testfile.txt', "r") as testfile:
        readtest = testfile.readlines()
    for line in range(4,5,1): #test for post rates
        linefromfile = readtest[line]
        jsonfromtext = json.loads(linefromfile)
        payload = jsonfromtext['POST']
        r = requests.post(url=URL, data=payload)
        try:
            r_dict = json.loads(r.text)
            linefromfile = readtest[line].replace('valuetochange', '{0}'.format(r_dict['id']))
        except json.decoder.JSONDecodeError:
            linefromfile = readtest[line]
        jsonfromtext2 = json.loads(linefromfile)
        testvalue = jsonfromtext2['return']
        test = check(str(r.text).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""),
                     str(testvalue).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""))
        # test = check(r.status_code, "400")
        if test == 1:
            break
    # test for get rates
    rget = requests.get(url=URL)
    firstget = rget.json()[0]['rate']
    test = check(str(firstget),"400")
    jsonfromtext = json.loads(readtest[6])
    payload = jsonfromtext['POST']
    rpost = requests.post(url=URL, data=payload)
    rget = requests.get(url=URL)
    secget = rget.json()[0]['rate']
    test1 = check(str(secget),"1500")

    if test1==0 and test==0:
        return test
    return 1
def trucktest(provider_id):
        URL = "http://localhost:8085/api/trucks"
        with open(f'testfile/testfile.txt', "r") as testfile:
            readtest = testfile.readlines()
        for line in range(8, 10, 1):  # test for post trucks
            linefromfile = readtest[line].replace('valuetochange', str(provider_id))
            jsonfromtext = json.loads(linefromfile)
            payload = jsonfromtext['POST']
            r = requests.post(url=URL, data=payload)
            testvalue = jsonfromtext['return']
            test = check(str(r.text),str(testvalue))
            if test == 1:
                return "POST to http://localhost:8085/api/trucks test not good"
        # test for get rates
        rget = requests.get(url=URL)
        test = check(rget.text,"Please enter truck license plate and provider id:")
        if test == 1:
            return "get to http://localhost:8085/api/trucks test not good"
        for line in range(13, 15, 1):  # test for put trucks
            linefromfile = readtest[line].replace('valuetochange', str(provider_id))
            jsonfromtext = json.loads(linefromfile)
            payload = jsonfromtext['PUT']
            truck_id = jsonfromtext['value']
            URL = "http://localhost:8085/trucks/"+str(truck_id)
            r = requests.put(url=URL, data=payload)
            testvalue = jsonfromtext['return']
            test = check(str(r.text), str(testvalue))
            if test == 1:
                return "PUT to http://localhost:8085/trucks test not good"
        for line in range(18, 19, 1):  # test for get truck
            linefromfile = readtest[line].replace('valuetochange', str(provider_id))
            jsonfromtext = json.loads(linefromfile)
            payload = jsonfromtext['GET']
            truck_id = jsonfromtext['value']
            URL = "http://localhost:8085/truck/" + str(truck_id)
            r = requests.get(url=URL, params=payload)
            if r.status_code == 200:
                try:
                    r.json()
                    test = 0
                except json.decoder.JSONDecodeError:
                    return "GET to http://localhost:8085/api/truck/<truck_id> test not good"
            elif r.status_code == 404:
                testvalue = jsonfromtext['return']
                test = check(str(r.text), str(testvalue))
            if test == 1:
                return "GET to http://localhost:8085/api/truck/<truck_id> test not good"
        return 0
def cleartestdatabases(provider_id):
    with open(f'testfile/testfile.txt', "r") as testfile:
        readtest = testfile.readlines()
        linefromfile = readtest[24].replace('valuetochange', str(provider_id))
        jsonfromtext = json.loads(linefromfile)
        payload = jsonfromtext['GET']
        print(payload)
        URL = "http://localhost:8085/clear/"
        r = requests.get(url=URL, params=payload)
        print(r.status_code)
        print(r.url)
        return 0
def main():
    first = checkhealth()
    checkprov  = checkprovider()
    print(checkprov)
    sectest = checkprov[0]
    provider_id_test = checkprov[1]
    thertest = checkrates()
    forth  = trucktest(provider_id_test)
    print(sectest, first, thertest, forth)
    cleartestdatabases(provider_id_test)
    if first == 0 and sectest == 0 and thertest == 0 and forth == 0:
        print("no error found")
        return 0
    else:
        return 1


main()