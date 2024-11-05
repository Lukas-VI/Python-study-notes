#PRINT
import time as t
for i in range(100+1):
    print("\r{:3}%".format(i),end="")
    #                       加,end= 不换行,一行里接着打
    t.sleep(0.1)
