#!/usr/bin/Python
import json
import time
import winsound
from alert_list import alert_list





def alert():
   
    #obj = alert_cls.alert_list = 
    while True:
        if json.loads(alert_list())>40:
            
            winsound.Beep(500,500)
            time.sleep(3)
            print '%s overset'
            


if __name__ == '__main__':
    alert()