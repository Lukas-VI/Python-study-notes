#Sn
def sn(n):
    for i in range(n+1):
        sum = 0
        if i%2 == 0:
            sum -= 2*n - 1
        else:
            sum += 2*n - 1
    return sum

if __name__ == "__main__":
    print("Sn = ",sn(int(input("Please in put an int : "))))
