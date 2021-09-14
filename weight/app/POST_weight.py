from re import template
from flask import request
from mysql_db import mysql_db
import time 
import json

mySQL = mysql_db()

def POST_weight():
        
    dir = request.args.get('direction')
    containers = request.args.get('containers')
    weight = request.args.get('weight')
    unit = request.args.get('unit')
    force = request.args.get('force')
    product = request.args.get('product', 'NA')
    truck_id = request.args.get('truckid')
    
    date = time.strftime('%Y%m%d%H%M%S')
    
    # container_weight = mySQL.getData(f'SELECT weight from containers WHERE id = "{containers}"')
    # neto = netoWeight(float(weight), container_weight[0]['weight'])
    
    last_dir = mySQL.getData(f'select direction from sessions where trucks_id = {truck_id} order by date desc limit 1')[0]['direction']
    
    if last_dir == dir and force == True:
        mySQL.setData(f'UPDATE sessions SET bruto = {weight} WHERE trucks_id = {truck_id} order by date desc limit 1')
        
    elif last_dir == dir and force == False: 
        return f'Error in direction -> caused by {truck_id}'
    
    elif dir == 'in' or dir == 'none':
            createNewSession(dir, force, date, weight, truck_id, product)
            return 'Finished!'
        
    elif dir == 'out':
        session_id = mySQL.getData(f'select id, date from sessions where trucks_id = {truck_id} order by date desc limit 1')
        session_id = session_id[0]['id']
        return f'{session_id}'
    
    else:
        return 'Error in direction'

def createNewSession(direction, f, date, weight, truckid, product):
    product_id = mySQL.getData(f'select id from products where product_name = "{product}" limit 1')
    data = (direction, f, date, weight, truckid, product_id[0]['id'])
    query = (f'INSERT IGNORE into sessions (direction, f, date, bruto, trucks_id, products_id) VALUES (%s, %s, %s, %s, %s, %s)')
    mySQL.setData(query, data)
    
    
def netoWeight(bruto, neto):
    return bruto - neto;
