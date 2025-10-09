def is素数(num):
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
            break
    return flag

for i in range(2,501):
    if is素数(i):
        print(i,end="\t")

