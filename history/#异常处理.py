#异常处理
try:
    n=eval(input("input a int"))
    print(n)

except NameError:               #加入错误条件
    print("num ERROR")
except:
    print("ERROR")
else:
    print("well")           #本语句不发生异常时进行
finally:
    print("3 is finally well")        #4一定执行