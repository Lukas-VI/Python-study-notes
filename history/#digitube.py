#digitube
import turtle as tu
import time as t
def line(d):
    tu.pendown() if d else tu.penup()
    tu.fd(40)
    tu.right(90)
def dd(digi):
    line(True) if digi in [2,3,4,5,6,8,9] else line(False)
    line(True) if digi in [0,1,3,4,5,6,8,9] else line(False)
    line(True) if digi in [0,2,3,5,6,8,9] else line(False)
    line(True) if digi in [0,2,6,8] else line(False)
    tu.left(90)
    line(True) if digi in [0,4,5,6,8,9] else line(False)
    line(True) if digi in [0,2,3,5,6,7,8,9] else line(False)
    line(True) if digi in [0,1,2,3,4,7,8,9] else line(False)
    tu.left(180)
    tu.penup()
    tu.fd(20)
def date(date):
    
    for i in date:
        dd(eval(i))
def main() :
    tu.setup(800,350,200,200)
    tu.penup()
    tu.bk(300)
    tu.pensize(5)
    date('20240617')
    tu.hideturtle()
main()