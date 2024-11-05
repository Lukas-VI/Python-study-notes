#TEXTPROBAR
import time as t
s=296
print("{0:=^300}".format("start"))
for i in range(s+1):
    a='■'*i
    b='□'*(s-i)
    c=(i/s)*100
    print("{:3.0f}%{}{}".format(c,a,b))
    t.sleep(0.01)
print("{0:=^300}".format("end"))