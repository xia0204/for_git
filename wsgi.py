#!/usr/bin/env python
#coding:utf-8



from wsgiref.simple_server  import make_server



def RunSever(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return '<h1>hello,world</h1>'
	
	
	
if __name__ ==  '__main__':
	httpd = make_server('',8000,RunSever)
	print "serving http on port 8000..."
	httpd.serve_forever()