from flask import request
import time 

def POST_weight():
        
    dir = request.args.get('direction')
    truck = request.args.get('truck', 'NA')
    containers = request.args.get('containers')
    weight = request.args.get('weight')
    unit = request.args.get('unit')
    force = request.args.get('force')
    produce = request.args.get('produce', 'NA')
    
    date = time.strftime('%Y%m%d%H%M%S')
    
    if dir == 'in' or dir == 'none':
        createNewSession()
        
        
def createNewSession(direction, f, date, weight):
    pass
    