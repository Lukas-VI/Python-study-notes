#file
n=open("hamlet.txt","r")
txt=n.readlines(1)
while txt != []:
    txt=n.readlines(1)
    print(txt)
n.close