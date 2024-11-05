#使用遍历列表的方法，输出像素爱心


from time import sleep


a = [0,1, 1,0,  1, 1, 0]
b = [7, 5 , 3,1]
c=[0,1,2,3]
for i in a:  # 遍历列表a
    if i == 1:  # 如果a[i]为1，则输出▧
        print("▧", end="")
    else:  # 如果a[i]为0，则输出空格
        print(" ", end="")
print()  # 换行

# 可以根据需要继续输出其他行
for i in b :
    print(" " *int((7-i)/2) , end="")
    print("▧"*i,end="")    
    print()


sleep(13.14)  # 等待13.14秒