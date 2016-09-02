#!/usr/bin/Python


import sys
import time
import threading
import multiprocessing

def deco_thread(fun):
    t = threading.Thread(target=fun)
    t.start()
'''def deco_mulpro(fun):
    m = multiprocessing.Process(target=fun)
    m.start()
    return fun
'''
#@deco_thread
#@deco_mulpro
def a():
    print "astart:"+str(time.ctime())
    time.sleep(3)
    print 'aend:'+str(time.ctime())
    return
#@deco_thread
#@deco_mulpro
def b():
    print 'bstart:'+str(time.ctime())
    time.sleep(8)
    print 'bend:'+str(time.ctime())
    return
def c():
    print 'worked'
    return
'''dic_t = {'a':a,'b':b}
for i in range(len(dic_t.keys())):
    
    t = threading.Thread(target=dic_t.values()[i])
    t.start()
sys.exit()'''
'''if  __name__ == '__main__':
    dic_t = {'a':a,'b':b,'c':c}
    for i in range(len(dic_t.keys())):
    #for i in range(5):
            t = multiprocessing.Process(target=dic_t.values()[i])
            t.start()
'''

reflite = raw_input('input module: ')
reflite = reflite.split('/')
module = __import__(reflite[0])
cpu_test = getattr(module,reflite[1])
cpu_test()
print dir(module)





