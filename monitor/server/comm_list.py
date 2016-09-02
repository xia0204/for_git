#!/usr/bin/python
import platform
from win_pluggins.Basepluggins import ls,mem,cpu,exit
from linux_pluggins import *
#comm_list = None
win_comm_list = {'ls':ls,'cpu':cpu,'mem':mem,'exit':exit}
linux_comm_list = {'ls':l_ls,'cpu':l_cpu}
other = {}
def comm():
    if platform.system() == 'Linux':
        return linux_comm_list
    elif platform.system() == 'Windows':
        return win_comm_list
    else:
        return  other
comm_list = comm()