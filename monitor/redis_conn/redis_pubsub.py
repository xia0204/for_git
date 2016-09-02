#!/usr/bin/Python
#coding:utf-8
import json
import redis




redis_mon = redis.Redis(host = '192.168.3.90',port = 6379)
sub = redis_mon.pubsub()
sub.subscribe('test')
for item in sub.listen():
    if item['type'] == 'message':
        if item['data'] == 3:
            print 'warning!!!' 
            