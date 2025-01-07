#chu so cuoi cung lon nhat
from math import *
def snt(n):
    if n < 2 :
        return 0
    for i in range(2, isqrt(n)+1) :
        if n % i == 0:
            return 0
    return 1
def check(n):
    if(snt(n)):
        donvi = n%10
        while n != 0:
            if n%10 > donvi:
                return False
            n //= 10
        return True
    return False
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        dem = 0
        for i in range(1, n + 1):  # Bao gồm cả n
            if check(i):
                print(i, end=' ')
                dem += 1
        print()
        print(dem)