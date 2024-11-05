#set
#集合是多个元素的无序组合一集合类型.与数学中的集合概念一致一.集合元素之间无序，每个元素唯一，不存在相同元素一集合元素不可更改，不能是可变数据类型d
import random as r
r.seed(10)
a={1,2,3,1,1}
b=set("11122222222233333333333TTTTTWETQWETR")
print(a,b)
print(a-b)
print(b-a)
print(a^b)
print(a&b)
print(a|b)
print(a.add("c"))
print(b.discard("1"))
c={"c","s","ss","ssr","r","ssr"}
try:
    while True:
        print(c.pop(),end="  ")
except:
    pass
#数据去重
