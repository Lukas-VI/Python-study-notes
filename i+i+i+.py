def f(n):
    p = 1 if n % 2 != 0 else -1
    return 1 / (n * (n + 1)) * p
    
if __name__ == "__main__":
    b = 0.0
    for n in range(1,int(input("input : ")) + 1):
        b = b + f(n)
    print(b)

