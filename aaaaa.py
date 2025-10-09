def f(n):
    i, b = 1, 0
    p = 1 if n % 2 != 0 else 2
    while i < n:
        yield b
        b = b + 1 / (i + p)
        i = i + 1

if __name__ == "__main__":
    for n in f(int(input("input n: "))): 
        pass
    print("%.2f" % n)