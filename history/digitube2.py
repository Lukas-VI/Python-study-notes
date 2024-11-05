#digitube2
import turtle as tu
import time as t
def dg():
    tu.penup()
    tu.fd(6)
def line(d):
    dg()
    tu.pendown() if d else tu.penup()
    tu.fd(40)
    tu.right(90)
def dd(digi):
    line(True) if digi in [2,3,4,5,6,8,9] else line(False)
    line(True) if digi in [0,1,3,4,5,6,7,8,9] else line(False)
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
    tu.pencolor("red")
    for i in date:
        if i=="y":
            tu.write("year",font=("Arial",18,"normal"))
            tu.fd(50)
        elif i=="m":
            tu.write("month",font=("Arial",18,"normal"))
            tu.fd(40)
        elif i=="d":
            tu.write("day",font=("Arial",18,"normal"))    
            tu.fd(40)
        else:
            dd(eval(i))
def main() :
    tu.setup(800,350,200,200)
    tu.penup()
    tu.bk(300)
    tu.pensize(5)
    date(t.strftime("%Yy%mm%dd",t.gmtime())) 
    tu.hideturtle()
    tu.done()
main()