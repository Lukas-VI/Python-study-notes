#pypy                              
import turtle                   #引用库,不容易重函数名
#库名.函数名
turtle.setup(1550,550,0,0)      #窗体位置与大小布局setup(长,宽,横坐标,纵坐标) 左上角是(0,0) 
turtle.penup()                  #t.pu飞
turtle.fd(-250)                 #fd前 bk后 运行相对运动
turtle.pendown()                #t.pd落
turtle.pensize(25)              #t.width
turtle.pencolor("purple")       #色彩名称还有seashell,gold,pink,brown,tomato...... RGB型:t.pencoloe(R,G,B)/((R,G,B))
turtle.colormode(1.0)           #RGB小数
turtle.colormode(255)           #RGB整数
turtle.seth(-40)                #设置绝对方向
                                #turtle.left/right(angle) 向左/右转,相对方向
for i in range(6):              #循环结构 for 变量 in range(次数) i=0到次数-1
                                #range(N)产生从0开始的N个整数列 range(N,M)从N输出到M-1
    turtle.circle(40,90)        #(r,角度),从相对t左侧r处为半径
    turtle.circle(-40,180)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(80*2/3)
#turtle.done()
#不写库名
from turtle import*        #加*或函数名,方便
#setup(1550,550,0,0)      #窗体位置与大小布局setup(长,宽,横坐标,纵坐标) 左上角是(0,0) 
penup()                  #
goto(-500,200)
fd(-250)                 #fd前 bk后 运行相对运动
pendown()
pensize(45)
pencolor("purple")       #色彩名称还有seashell,gold,pink,brown,tomato......
colormode(1.0)           #RGB小数
colormode(255)           #RGB整数
seth(-40)                #设置绝对方向
                                #turtle.left/right(angle) 向左/右转,相对方向
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(16,180)
fd(80*2/3)
done()
import turtle as t       #给turtle起名为t 两全
print ("a",    i )
