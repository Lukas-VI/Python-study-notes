#hamlet
def gt():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in "`~!@#$%^&*(?)_+""=[>/:]{,<'.}\|';" :
        txt=txt.replace(ch," ")
    return txt
ht=gt()
ws=ht.split()
dc={}
for w in ws:
    dc[w]=dc.get(w,0)+1
item=list(dc.items())
item.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    w,dc=item[i]
    print("{0:<10}{1:>5}".format(w,dc))
