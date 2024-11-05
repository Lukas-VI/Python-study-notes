import turtle
import math

def draw_gear(turtle, radius, teeth):
    angle = 2 * math.pi / teeth
    for _ in range(teeth):
        turtle.forward(radius)
        turtle.right(angle)

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    gear = turtle.Turtle()
    gear.speed(1)
    gear.color("gray")
    gear.fillcolor("gray")

    # 画齿轮
    gear.begin_fill()
    draw_gear(gear, 50, 10)  # 画一个齿轮，半径为50，齿数为10
    gear.end_fill()

    window.mainloop()

main()
