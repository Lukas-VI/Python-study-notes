#random库
#basic:seed(),random()
#用种子产生序列,种子一样,数列一样
import random as r
r.seed(14)
for i in range(10):
    print("{:.2f}".format(r.random()))
    #print(round(r.random(),2))
    print(r.randint(10,100))               #生成范围内的随机整数
    print(r.randrange(1,10,2))           #range(a,b,step)
    print(r.getrandbits(8))                 #生成k比特长的
    print(r.uniform(12,13))                    #生成范围内小数16f
    print(r.choice([1,2,3,4,5,6]))              #选择序列
    s=[1,2,3];r.shuffle(s);print("{}".format(s).strip(" "))#打乱后输出,用";"打多行                 