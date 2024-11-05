import os as o
def a(an) : 
    if o.path.isfile(an+'.png')==False:
        return 1
    else:
        return 0
an=input("gafsasg")
print(a(an))