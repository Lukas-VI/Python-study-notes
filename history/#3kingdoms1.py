#3kingdoms1
import jieba as j
txt=open("threekingdoms.txt","r",encoding="utf-8").read()
ws=j.lcut(txt)
ex={"将军","却说","荆州","二人","不可","不能","如此"}
sum=0
dc={}
for w in ws:
    if len(w)==1 or w in ex:
        continue
    #elif w=="刘备曰"or w==""
    else:
        dc[w]=dc.get(w,0)+1
item=list(dc.items())
item.sort(key=lambda x:x[1],reverse=True)
rad=0
for i in range(15):
    w,dc=item[i]
    sum+=dc
dc=0
for i in range(15):
    w,dc=item[i]
    rad=dc/sum
    print("{0:<10} {1:>5} ".format(w,dc))
    print("{0:,.2%} ".format(rad))
