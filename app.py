#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask, jsonify, request, abort
from flask_mysqldb import MySQL
from flask_selfdoc import Autodoc

import logging
import os
import unicodedata


app = Flask(__name__)
auto = Autodoc(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'nakamura'
app.config['MYSQL_DB'] = 'intelipost'

mysql = MySQL(app)

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s level=%(levelname)s message=%(message)s')


@app.route('/', methods=['GET'])
@auto.doc()
def index():
    return "App to save deploy events"

@app.route('/add', methods=['POST'])
@auto.doc()
def insert():
    """
    POST: Save envents on database according JSON.
    Ex: curl --header "Content-Type: application/json" -XPOST -d \
    '{
        "component": "AppZ",
        "id": 3,
        "owner": "Gabriel",
        "start": "2019-05-28 22:30:20",
        "finish": "2019-05-28 22:45:20",
        "version": 1.0.0
    }' \
    http://localhost:5000/add
    """
    try:
        jsoninfo = request.get_json()
        jsoninfo['start'] = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        jsoninfo['finish'] = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
        _id = jsoninfo['component']
        _version = jsoninfo['version']
        _owner = jsoninfo['owner']
        cur = mysql.connection.cursor()
        query = "INSERT INTO deploy_infos (id, component, version, owner, start, finish) VALUES ('%(id)s', '%(component)s', '%(version)s', '%(owner)s', '%(start)s', '%(finish)s')" %(jsoninfo)        
        print(query)
        cur.execute(query)
        # INSERT INTO deploy_infos (id, component, version, owner, start, finish) VALUES ('2', 'AppY', '1.0.0', 'Mike', '2019-05-28 21:49:30', '2019-05-28 21:56:30');
        mysql.connection.commit()
        logging.info('A new deploy info has been saved.')
        cur.close()
        return jsonify({"info": "Ok"})
    except Exception as e:
        s = str(e)
        logging.error('MySQL connection is NOT OK!')
        return jsonify({"info": "Something is wrong!" + s})

@app.route('/list', methods=['GET'])
@auto.doc()
def list():
    """
    GET: List all events saved in database
    Ex: curl -X "GET" http://localhost:5000/list
    """
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM deploy_infos")
    data = cur.fetchall()
    datalist = []
    if data is not None:
        for item in data:
            datatempobj = {
                'id': item[0],
                'componet': item[1],
                'version': item[2],
                'owner': item[3],
                'start': item[4],
                'finish': item[5]
            }
            datalist.append(datatempobj)
        return jsonify(datalist)

@app.route('/list/<id>', methods=['GET'])
@auto.doc()
def list_id(id):
    """
    GET: Search an event in database based in ID passing throw URI.
    Ex: curl -X "GET" http://localhost:5000/list/4
    """
    try:
        unicodedata.numeric(id)
        cur = mysql.connection.cursor()
        query = """SELECT * FROM deploy_infos where id=%s"""
        cur.execute(query, (id, ))
        data = cur.fetchall()
        datalist = []
        if data is not None:
            for item in data:
                datatempobj = {
                    'id': item[0],
                    'componet': item[1],
                    'version': item[2],
                    'owner': item[3],
                    'start': item[4],
                    'finish': item[5]
                }
                datalist.append(datatempobj)
            return jsonify(datalist)
    except:
        logging.error('Something is worng!')
        return ('something is wrong!')

@app.route('/status')
@auto.doc()
def healthcheck():
    """
    Ex: curl -XGET http://localhost:5000:port/status
    """
    try:
        cur = mysql.connection.cursor()
        logging.info('MySQL connection is OK!')
        return jsonify({"mysql": "up"})
    except Exception:
        logging.error('MySQL connection is NOT OK!')
        return jsonify({"mysql": "down"})

@app.route('/help')
@auto.doc()
def documentation():
    return auto.html()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')