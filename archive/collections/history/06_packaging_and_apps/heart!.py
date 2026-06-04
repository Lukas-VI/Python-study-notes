from time import sleep
import turtle

# 设置海龟
t = turtle.Turtle()
t.speed(5)  # 设置绘制速度
t.color("red")  # 设置颜色

# 开始绘制心形
t.begin_fill()  # 开始填充
t.left(140)  # 左转140度
t.forward(224)  # 向前绘制224个单位
t.circle(-112, 200)  # 画一个半径为112，弧度为200的圆
t.left(120)  # 左转120度
t.circle(-112, 200)  # 再画一个半径为112，弧度为200的圆
t.forward(224)  # 再次向前绘制224个单位
t.end_fill()  # 结束填充

# 完成绘制
t.hideturtle()  # 隐藏海龟光标
turtle.done()  # 完成事件循环


#使用遍历列表的方法，输出像素爱心





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


