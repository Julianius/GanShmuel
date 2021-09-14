import requests
import json

def check(thecheck, therespone):
    if str(thecheck) == str(therespone):
        return 0
    else:
        return 1


def checkhealth():
    urlname = ['health', 'providers.html', 'rates.html', 'trucks.html']
    for url in urlname:
        URL = "http://localhost:8081/{0}".format(url)
        res = requests.get(url=URL)
        test = check(res.status_code, "200")
        if test == 1:
            break
    return test


def checkprovider():
    URL = "http://localhost:8081/api/providers.html"
    with open(f'testfile/testfile.txt', "r") as testfile:
        readtest = testfile.readlines()
    for line in range(0,2):
        linefromfile = readtest[line]
        jsonfromtext = json.loads(linefromfile)
        payload = jsonfromtext['POST']
        r = requests.post(url=URL, data=payload)
        try:
            r_dict = json.loads(r.text)
            linefromfile = readtest[line].replace('valuetochange', '{}'.format(r_dict['id']))
        except json.decoder.JSONDecodeError:
            linefromfile = readtest[line]
        jsonfromtext2 = json.loads(linefromfile)
        testvalue = jsonfromtext2['return']
        test = check(str(r.text).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""),
                     str(testvalue).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""))
        # test = check(r.status_code, "400")
        if test == 1:
            break
    return test


def checkrates():
    URL = "http://localhost:8081/api/rates.html"
    with open(f'testfile/testfile.txt', "r") as testfile:
        readtest = testfile.readlines()
    for line in range(4,5,1):
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

def main():
    first = checkhealth()
    sectest = checkprovider()
    thertest = checkrates()
    print(sectest, first, thertest)
    if first == 0 and sectest == 0 and thertest == 0:
        print("no error found")
        return 0
    else:
        return 1


main()
