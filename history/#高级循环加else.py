#高级循环加else
#正常循环后,再执行else额外奖励
#如果被break,else就不会被执行
for i in range(9):
    if i==8:
        break 
    print(i)
else:
    print("no break")
a=1
while a!=10:
    a=a+1
    print(a)
else:
    print("ok")
