from requests.api import request
from mysql_db import mysql_db
from datetime import datetime

def GET_weight(request):
    mySQL = mysql_db()
    # try:
    fromTime = request.args.get('from') if request.args.get('from') else datetime.now().strftime("%Y%m%d000000")
    toTime = request.args.get('to') if request.args.get('to') else datetime.now().strftime("%Y%m%d%H%M%S")
    filter = f"('{request.args.get('filter')}')" if request.args.get('filter') else "('in', 'out', 'none')" 
    query="""SELECT t1.id, direction, bruto, neto, product_name, GROUP_CONCAT(t3.containers_id) as containers
        FROM sessions AS t1 
        JOIN products AS t2 
        ON t1.products_id = t2.id 
        JOIN containers_has_sessions as t3 
        ON t1.id = t3.sessions_id 
        WHERE t1.date BETWEEN  '{0}' AND '{1}'
        AND direction IN {2}
        GROUP BY t3.sessions_id"""
    info = mySQL.getData(query.format(fromTime, toTime, filter))			
    return str(info)
    # except:
        # return "Weight data is unavailable at the moment."