#write
fo=open("o.txt","w+t")
ls=["a","2","u"]
fo.writelines(ls)
fo.seek(1)
for line in fo:
    print(line)
fo.close()