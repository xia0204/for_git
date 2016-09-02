#!/usr/bin/Python

import sys
import time
import paramiko

from twisted.spread.pb import respond
username = 'root'
passwd = 'devops'
host = '192.168.3.90'
passinfo = '\'s password: '
cmd = raw_input('command>')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.3.90', 22, 'root', 'devops')
channel = ssh.invoke_shell()
channel.settimeout(100)

channel.send('ssh '+username+'@'+host+'\n')
buff = ''
resp = ''

'''while 1:
    if not buff.endswith("'s password:"):
        resp = channel.recv(9999)
        buff += resp
        print buff
    else:
        break'''
while not buff.endswith(passinfo):
    resp = channel.recv(9999)
    buff+=resp
    print buff



channel.send(passwd+'\n')
buff = ''
while not buff.endswith('# '):
    resp = channel.recv(9999)
    buff+=resp
    if not buff.find(passinfo)==-1:
        print 'renzheng shibai'
        channel.close()
        ssh.close()
        sys.exit()
    print buff
    
    
channel.send('%s\n'%cmd)
buff = ''
try:
    while buff.find('#') == -1:
        resp = channel.recv(9999)
        buff = buff+resp
except Exception,e:
    print 'error for ifconfig'
print buff
channel.close()
ssh.close 
         
#channel.send('ifconfig')
#channel.close()
#ssh.close()                 

'''chan = ssh.invoke_shell()
chan.settimeout(10)

buff = ''
resp = ''
chan.send('ssh %s@%s \n'%(username,host))
while not buff.endswith(passinfo):
    try:
        resp =chan.recv(9999)
    except Exception,e:
        print 'error %s'%str(e)
        chan.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no')== -1:
        chan.send('yes')
        buff = ''
chan.send(passwd+'\n')


buff = ''
while not buff.endswith('#'):
    resp = chan.recv(9999)
    if not resp.find(passinfo) == -1:
        print 'errot info:faild'
        chan.close()
        sys.exit()
    buff = ''
chan.send('cmd')

buff = ''
try:
    while buff.fnd('#') == -1:
        resp = chan.recv(9999)
        buff += resp
except Exception,e:
    print 'error info %s'%str(e)


print buff
    
    
chan.close()    
        


ssh.close()'''