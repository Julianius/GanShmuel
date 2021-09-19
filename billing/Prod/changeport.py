import os
import sys
with open(f'billing.py', "r") as readchange:
    readit=readchange.read()
    readit=readit.replace("5000" , str(int(sys.argv[1])+2))
with open(f'billing.py', "w") as readchange:
    readchange.write(readit)
listfile=["bills.html","trucks.html","truck_id.html","rates.html","providers.html","index.html","health.html","bills_spec.html"]
for file in listfile:
    print(file)
    with open(f'templates/{file}', "r") as readchange:
        readit = readchange.read()
        readit = readit.replace("localhost:8081", "3.123.232.208:"+str(int(sys.argv[1])))
    with open(f'templates/{file}', "w") as readchange:
        readchange.write(readit)
