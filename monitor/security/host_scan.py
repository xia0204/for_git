#!/usr/bin/Python

import sys
import nmap
import json
from host_list import host_list
#from IPython.core.magic_arguments import argument

def host_scan():
    print('the host which you can scan are  as follow:%s'%json.dumps(host_list.keys())+'\n'+'or you \
can type host like "192.168.0.1/24"')
    hostname = raw_input('now please select a host you want to scan>')
    port = raw_input('please input the port which you want to scan for this host>')
    #get the information from user type 
    if hostname in host_list.keys():
        hostname = host_list[hostname]
        port = port
    
    try:                                     #try instance scanner
        nm = nmap.PortScanner()
    except nmap.PortScannerError:
        print('namp not found',sys.exc_info()[0])  #got the error
        sys.exit(0)
    try:
        nm.scan(hosts = hostname,arguments = '-v -sS -p'+port)  #try execute scan for type 
    except Exception,e:
        print "Scan error"+str(e)
        
        #get result and print 

    for host in  nm.all_hosts():
        print('-'*60)
        print('Host:  %s(%s)' %(host,nm[host].hostname()))
        print('State:  %s'%nm[host].state())
        for proto in nm[host].all_protocols():
               
            print('Protocol : %s'%proto)
                
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                print('port:%s \t state: %s'%(port,nm[host][proto][port]['state']))
                                 
if __name__ == '__main__':
    host_scan()
                    
        