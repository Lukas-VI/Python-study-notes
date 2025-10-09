n = int(input("请输入项数n: "))
sn = 0
for i in range(1, 2 * n, 2):
    if (i // 2) % 2 == 0:
        sn += i
    else:
        sn -= i
print("S_n的值为:", sn)
