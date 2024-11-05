#无限(条件)循环
#保留字break结束所有循环,continue跳过本次循环
s="1234567890"
import time as t
ts=t.perf_counter()
while s !="":
    for c in s:
        if c=="0":
            break
        elif c=="5":
            continue
        print("*".join("{}".format(s).center(10," ")))
        s=s[:-1]
    if (t.perf_counter()- ts)>2:
        break