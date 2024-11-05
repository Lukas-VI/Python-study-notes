#strrevs
def strvs(a):
    if a =="":
        return ""
    else:
        return strvs(a[1:])+a[0]
print(strvs(input()))
print(input()[::-1])

