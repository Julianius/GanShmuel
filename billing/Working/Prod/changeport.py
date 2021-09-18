import os
import sys
with open(f'billing.py', "r") as readchange:
    readit=readchange.read()
    readit=readit.replace("5000" , str(int(sys.argv[1])+2))
with open(f'billing.py', "w") as readchange:
    readchange.write(readit)