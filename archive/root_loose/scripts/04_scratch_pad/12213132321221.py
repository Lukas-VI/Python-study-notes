def func(a,b):
    if a>b:  
        a,b=b,a  
    r=1  
    while r!=0:  
        r = a % b
        a = b 
        b = r
    return a
m=eval(input("请输入一个整数："))
n=eval(input("请输入一个整数："))
print(func(m,n))