#DDU4
df=0.01
dfm=input("dfm")
def du(df):
    du=1
    for i in range(365):
        if i % 7 in [0,6]:
            du=du*(1-df)
        else:
            du=du*(1+df)
    return du
dum=pow(1+eval(dfm),365)
while du(df) <dum:
    df+=0.001
print("df is {:.2f},dum is {:.2f}".format(df,dum))