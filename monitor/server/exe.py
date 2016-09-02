#!/usr/bin/python
#from win_pluggins import *
from comm_list import comm_list
import json
import re

result = ''
def execute():
	global result 
	comm = raw_input('>')
	if comm in comm_list.keys():
		try:
			comm_list['%s'%comm]()
		except Exception,e:
			print e 
	else:
		result = 'please input comm in %s'%json.dumps(comm_list.keys())
		print result
	return result
if __name__ == '__main__':
	#add the alert module
	while 1:
		execute()
