from mysql_db import mysql_db
import os
import json


def POST_batch_weight(filename):
    mySQL = mysql_db()
    query = "INSERT IGNORE INTO containers (id, weight, unit) VALUES (%s,%s,%s)"
    path = 'in/'
    
    if filename in os.listdir(path):

        # Lines for ---> csv <--- files
        if filename.endswith('.csv'): 
            f = open(f'in/{filename}')
            lines = f.readlines()
            
            unit = lines[0][:-1].split(',')[1]
            if unit[0] == '"' and unit[-1] == '"':
                unit = unit[1:-1]
            
            for line in lines[1:]:
                id = line.split(',')[0]
                weight = int(line.split(',')[1])
                data = (id, weight, unit)
                mySQL.setData(query, data)
                
        # Lines for ---> json <--- files
        elif filename.endswith('.json'):
            f = open(f"in/{filename}")
            lines = json.load(f)
            
            for line in lines:
                id = line['id']
                weight = line['weight']
                unit = line['unit']
                data = (id, weight, unit)
                mySQL.setData(query, data)
                
        f.close()
        return f'{filename}, Has been added to database.'
        
    else:
        return f'{filename}, Not Found.'