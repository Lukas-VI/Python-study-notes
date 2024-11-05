#DDU3
du=1.0
df=0.01
for i in range(365):
    if i % 7 in[6,0]:
        du=du*(1-df)
    else:
        du=du*(1+df)
print("du is  {:.2f}".format(du))
