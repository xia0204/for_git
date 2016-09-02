#!/usr/bin/Python
import sys
import json
import paramiko
from host_list import host_list

fort_ip = '192.168.3.90'
fort_port = 22
fort_user = 'root'
fort_passwd = 'devops'
passinfo = '\'s password: '

def short_fortress_ssh():
    print "this is the host you can connect:"+json.dumps(host_list.keys())# show host_list
    hostname = 'devops'#raw_input('please input the host you want to connect:') #get hostname
    if hostname  in host_list.keys():
        host,port,user,passwd = host_list[hostname]
        passwd_test = 'devops'
        cmd = 'ifconfig'#raw_input("now please input the command you want execute:")
    #connect modle
    else:
        print 'sorry the host you input are not in the list  '
        print 'or you can input the host which you want like 192.168.0.1'
        host = raw_input('please input host>')
        port = input('please input port>')
        user = raw_input('please input user>')
        passwd = raw_input('please input passwd>')
        cmd = raw_input('please input the command you want to execute>')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())#  don't have key for host
    ssh.connect(fort_ip,fort_port,fort_user,fort_passwd)#enter the fortress argument
    #creat invoke_shell for target host
    channel = ssh.invoke_shell()
    channel.settimeout(100)
       
    
    channel.send('ssh '+user+'@'+host+'\n')
    buff = ''
    resp = ''
    while not buff.endswith(passinfo):
        resp = channel.recv(9999)
        buff += resp
        print buff
 
 
    print 123
    channel.send(passwd+'\n')
    print 123
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
    
    '''channel.send(passwd_test+'\n')
    buff = ''
    while not buff.endswith('# '):
        resp = channel.recv(9999)
        buff += resp
        print buff
    if not buff.find(passinfo)==-1:
        print 'renzheng shibai'
        channel.close()
        ssh.close()
        sys.exit()
    print buff
    '''
    
    channel.send(cmd+'\n')
    buff = ''
    while not buff.endswith('#'):
        resp = channel.recv(9999)
        buff += resp
        print buff
    channel.close()
    #stdin,stdout,stderr = ssh.exec_command('%s'%cmd) #the command
    #stdout[1].read()
    
    ssh.close()
if __name__ == '__main__':
    
    short_fortress_ssh()



