#!/usr/bin/Python

import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',user='root',port=3306,passwd='root')
conn.select_db('mysql')

dbc = conn.cursor()
dbc.execute('show tables;')
for i in dbc.fetchall():
    print i
dbc.close()
conn.close()