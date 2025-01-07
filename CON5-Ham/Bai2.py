from math import *
def phantich(n):
    for i in range(2, isqrt(n)+1):
        mu = 0
        while n%i == 0:
            mu += 1
            n //= i
        if mu != 0:
            print(i,mu,sep = '^', end = '')
        if n != 1: #chua ptich xong
            print(' * ', end = '')
    if n > 1:
        print(n,1,sep = '^')

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        phantich(n)