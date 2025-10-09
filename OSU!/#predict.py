#predict
import csv
import sympy as sp

def get_list():
    list = []
    scv_reader = csv.reader(open(r'osu!.csv','r'))

    list += (int(eval(i[0])) for i in scv_reader)
    return list

# def c(x,a):
#     return math.log(x,a)

def liner(x,a,b):
    return  a * x + b

def lose(targrt,obj):
    return targrt - obj

def sum_lose(list,a,b):
    sum = 0
    squ = 0
    for i in list:
        sum += lose(list[squ],liner(squ,a,b))
        squ += 1
    return sum

def avg_loss(list):
    return sum_lose/len(list)

def diff(a,b):
    x = sp.symbols('a')
    f = liner(x,a,b)

    df_dx = sp.diff(f, x)
    return df_dx

if __name__ == "__main__":

    a = 1
    b = 0
    lose
    while loss >100
        lose = sum_lose(get_list(),a,b)
    print()
