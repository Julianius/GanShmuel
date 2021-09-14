<<<<<<< HEAD
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
    for line in range(len(readtest)):
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
        testvalue = jsonfromtext['return']
        test = check(str(r.text).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""),
                     str(testvalue).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""))
        # test = check(r.status_code, "400")
        if test == 1:
            break
    return test


def checkprovider():
    URL = "http://localhost:8081/api/providers.html"
    with open(f'testfile/testfile.txt', "r") as testfile:
        readtest = testfile.readlines()
    for line in range(len(readtest)):
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
        testvalue = jsonfromtext['return']
        test = check(str(r.text).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""),
                     str(testvalue).replace("\"", "\'").replace("\n", "").replace("\t", "").replace(" ", ""))
        # test = check(r.status_code, "400")
        if test == 1:
            break
    return test

def main():
    first = checkhealth()
    sectest = checkprovider()
    print(sectest, first)
    if first == 0 and sectest == 0:
        print("no error found")
        return 0
    else:
        return 1


main()
=======
return 0
>>>>>>> 8497beee2d57ce9bad90c04ac886adc242c8c2e0
