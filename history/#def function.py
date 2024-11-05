#def function
m=1
s=1000
def fact(n,m):  
    global s                                    #声明函数使用的是全局变量
    s=1                        #函数内定义的局部变量s与外部定义的s无关，重名了也不相同
    for i in range(1,n+1):
        s*=i
    return s                    
print(fact(3,3),s)          #此时s之全局变量s与函数内部运算无关
def fact(n,*b):         #可变参数*
    s=1
    for i in range(1,n+1):
        s*=i
    for item in b:
        s*=item
    return s,i      #输出元组类型
print(fact(3,3,3,3,3,3))        #允许输入多个输入
def a():
    print("a")
    return          #也可以什么都不返回
a()
ls=["1","2"]        #变量若为列表类型且函数内局部变量未被定义，局部变量就等同于全局变量
def lsa(a):
    ls.append(a)
    return
lsa("3")
print(ls)
def lsa(a):
    ls=[]
    ls.append(a)
    return
lsa("3")
print(ls)
