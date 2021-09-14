from flask import request
from mysql_db import mysql_db
import time 
import json

mySQL = mysql_db()

def POST_weight():
    
    try:
        dir = request.args.get('direction')
        containers = request.args.get('containers')
        weight = request.args.get('weight')
        unit = request.args.get('unit')
        force = request.args.get('force')
        product = request.args.get('product', 'NA')
        truck_id = request.args.get('truckid')
        
        date = time.strftime('%Y%m%d%H%M%S')
        
        tr_id = mySQL.getData(f'SELECT truckid from trucks WHERE id = {truck_id}')[0]['truckid']
        container_weight = mySQL.getData(f'SELECT weight from containers WHERE id = "{containers}"')[0]['weight']
        truck_weight = mySQL.getData(f'SELECT weight from trucks WHERE id = "{truck_id}"')[0]['weight']
        neto = netoWeight(float(weight), container_weight, truck_weight)
        
        last_dir = mySQL.getData(f'select direction from sessions where trucks_id = {truck_id} order by date desc limit 1')[0]['direction']
        
        if last_dir == dir and force == True:
            mySQL.updateData(f'UPDATE sessions SET bruto = {weight} WHERE trucks_id = {truck_id} order by date desc limit 1')
            
        elif last_dir == dir and force == False: 
            return f'Error in direction -> caused by {truck_id}'
        
        elif dir == 'in' or dir == 'none':
            createNewSession(dir, force, date, weight, truck_id, product)
            session_id = mySQL.getData(f'SELECT id from sessions WHERE trucks_id = {truck_id} order by date desc limit 1')
            session_id = session_id[0]['id']
            
        elif dir == 'out':
            mySQL.updateData(f'UPDATE sessions SET neto = {neto} WHERE trucks_id = {truck_id} order by date desc limit 1')
            session_id = mySQL.getData(f'select id, date from sessions where trucks_id = {truck_id} order by date desc limit 1')
            session_id = session_id[0]['id']
        
        if dir == 'in':
            value = {
                "id": session_id,
                "truck": tr_id,
                "bruto": weight
            }
            return json.dumps(value)
        
        elif dir == 'out':
            value = {
                "id": session_id,
                "truck": tr_id,
                "bruto": weight,
                "truckTara": truck_weight,
                "neto": neto
            }
            return json.dumps(value)
    
    except:
        return "Weight data is unavailable at the moment."

def createNewSession(direction, f, date, weight, truckid, product):
    product_id = mySQL.getData(f'select id from products where product_name = "{product}" limit 1')
    data = (direction, f, date, weight, truckid, product_id[0]['id'])
    query = (f'INSERT IGNORE into sessions (direction, f, date, bruto, trucks_id, products_id) VALUES (%s, %s, %s, %s, %s, %s)')
    mySQL.setData(query, data)
    
    
def netoWeight(bruto, c_weight, t_weight):
    return bruto - c_weight - t_weight;
