#!/usr/bin/python
import os
import sys
import time
import json
import psutil


#for redis 

def ls(self):
	'print the pwd'
	pwd = os.popen('dir')
	pwd = pwd.read()
	print pwd
	return pwd
	
def mem(self):
	for i in range(5):
		mem_info = psutil.virtual_memory()
		mem_info = json.dumps(mem_info)
		print mem_info
		time.sleep(1)
	return mem_info
	
def cpu(self):
	for i in range(3):
		info = psutil.cpu_percent()
		info = json.dumps(info)
		print info
		'''if int(sound) > 10:
			for i in range(5):
				if i < 4:
					winsound.Beep(500,500)
					time.sleep(0.5)'''
	return info 
	
	def exit(self):
		return sys.exit()