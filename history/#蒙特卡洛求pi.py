#蒙特卡洛求pi
from random import random
from time import perf_counter
d=pow(1000,2)*1
h=0.0
s=50
print("start".center(s+13,"="))
st=perf_counter()
p=0.000000
rt=0
rangt=perf_counter()
for i in range(1,d+1):
    p=1.000003912**i-1
    intime=perf_counter()
    x,y=random(),random()
    r=pow(x**2+y**2,0.5)
    if r <= 1.0:
        h=h+1
    a='■'*int(p)
    b='□'*(s-int(p)-2)
    c=00.0+(i/d)*100
    if rt>0.01:
        if round(c)==100:
            c=100
        dt=perf_counter() - st
        print("\r{:3.1f}%{}{}tc{:.2f}".format(c,a,b,dt),end="")
        rt=0
    outtime=perf_counter()
    rt=rt+(outtime-intime)
drangt=perf_counter()-rangt
pi=4*(h/d)
print("\n"+"pi is {}".format(pi))
print("total run time:{:.2f}".format(perf_counter()- st))
print("range time is {:.6f}, rad is{:,%}".format(drangt,(drangt/(perf_counter()-st)))) 
print("\n"+"end".center(s+13,"=")) 