import random as r
from re import U
import eventlet
import time
import os
def ping(ip):
    """Ping a single IP address and return the response time."""
    start_time = time.time()
    response = os.system(f"ping -c 1 -w 0.3 192.168.31.{ip-1}")
    end_time = time.time()

    if response == 0:
        return end_time - start_time
    else:
        print(f"Error pinging IP address: 192.168.31.{ip-1}")
        return 0
n=list(range(255))
un=r.sample(n,255)
for ip in un:
    response_time = ping(ip)
    print(f"IP address 192.168.31.{ip-1} replied in {response_time:.2f} seconds.")