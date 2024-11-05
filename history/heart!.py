
import turtle

# 设置海龟
t = turtle.Turtle()
t.speed(2)  # 设置绘制速度
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
