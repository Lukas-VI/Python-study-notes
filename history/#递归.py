 #递归  
def fact(n):        #递归是一种函数
    if n == 0:
        return 1  #基例
    else:  
        return n*fact(n-1)  #链条
print(fact(eval(input()))) 