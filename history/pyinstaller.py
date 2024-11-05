#pyinstaller
import turtle as t
def k(size,n):
    if n==0:
        t.fd(size)
    else:
        for a in [0,90,-90,-90,90]:
            t.left(a)
            k(size/3,n-1)
def main(s):
    t.speed(1000000000000000000000000000000000000000000)  
    t.penup()
    t.pendown()
    t.pensize(2)
    k(300,s)
    t.right(90)            
t.setup(1000,1000)
t.penup()
t.goto(-250,250)
for i in range(4):
    main(2)
t.hideturtle()
t.done()
      