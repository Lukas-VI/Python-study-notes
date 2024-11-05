#ping
#import gevent as g
#g.monkey.patch_all()
from os import system
import time as t
import eventlet as e  
e.monkey_patch()
for i in range(255):
    with e.timeout(0.5,False):
        system("ping 192.168.31.{}".format(i))