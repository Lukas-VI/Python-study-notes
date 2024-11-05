#AUtodraw
import turtle as t 
t.title("autodraw")
t.setup(1000,1000,0,0)
t.pencolor("red")
t.pensize(5)
data=[]
f=open("d.txt")
for line in f:
    line=line.replace("\n","")
    data.append(list(map(eval,line.split(","))))
f.close()
for i in range(len(data)):
    t.pencolor(data[i][3],data[i][4],data[i][5])
    t.fd(data[i][0])
    if data[i][1]==1:
        t.left(data[i][2])
    else:
        t.right(data[i][2])
t.done()  