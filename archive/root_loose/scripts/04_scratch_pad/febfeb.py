'''
def fab(x):
    if x == 0:
        result = 0
    elif x == 1:
        result = 1
    else:
        result = fab(x - 1) + fab(x - 2)
    return  result

'''
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

def fab_2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

class Fab_3(object):
    def __init__(self,max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
    
def fab_4(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        a, b = b, a + b 
        n = n + 1
 
if __name__ == "__main__":
    fab(100)

    for n in fab_2(100):
        print(n)

    for n in Fab_3(100):
        print(n)

    for n in fab_4(100): 
        print(n)