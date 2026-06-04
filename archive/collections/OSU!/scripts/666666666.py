def maxdiv(m, n):
    div = []
    for i in range(1, min(m, n) + 1):  # 遍历所有可能的公约数
        if m % i == 0 and n % i == 0:  # 判断是否为公约数
            div.append(i)
    print(m, "和", n, "的最大公约数是", div[-1])  # 输出列表最后一个元素（最大值）

x = int(input("num1:"))
y = int(input('num2:'))
maxdiv(x, y)