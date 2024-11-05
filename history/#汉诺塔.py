#汉诺塔
o=0 #
def h(n,src,dst,mid):
    global o
    if n==1:
        print("{}:{}>{}".format(1,src,dst))
        o+=1
    else:
        h(n-1,src,mid,dst)
        print("{}:{}>{}".format(n,src,dst))
        o+=1
        h(n-1,mid,dst,src)
h(3,"a","c","b")
print(o)
