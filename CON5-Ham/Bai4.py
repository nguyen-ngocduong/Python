#TONG UOC
from math import *
def tonguoc(n) :
    tong = 0
    for i in range(1, isqrt(n) + 1):
        if n%i == 0:
            tong += i
            if i != n/i :
                tong += n // i
    return tong
if __name__ == '__main__':
    n = int(input())
    print(tonguoc(n))