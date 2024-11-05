#sata
def gnum():
    num=[]
    instr=input("input num")
    while instr != "":
        num.append(eval(instr))
        instr=input("input num")
    return num
def dev(number,mean):
    sdev=0.0
    for num in number:
        sdev+=(num-mean)**2
    return pow(sdev/float(len(number)-1),0.5)
def mid(nums):
    sorted(nums)
    s=len(nums)
    if s%2==0:
        med=(nums[s//2-1]+nums[s//2])/2
    else:
        med=nums[s//2]
    return med
def mean():
    a=0
    for i in num:
        a+=i
    return a/len(num)
num=gnum()
print("med{}sdev{}".format(mid(num),dev(num,mean())))