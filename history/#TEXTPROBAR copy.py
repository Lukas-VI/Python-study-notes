#TEXTPROBARrefreshing
import time as t
s=50
print("start".center(s+7,"="))
ts=t.perf_counter()
for i in range(s+1):
    a='■'*i
    b='□'*(s-i)
    c=(i/s)*100
    d=t.perf_counter() - ts
    print("\r{:3.0f}%{}{}tc{:.2f}".format(c,a,b,d),end="")      #/r回到头
    t.sleep(1.1*i)
print("\n"+"end".center(s+7,"="))                               #/n换行
print("cost time:{:.2f}s".format(t.perf_counter()-ts))