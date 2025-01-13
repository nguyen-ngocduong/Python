#Liệt kê
from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
def tn(n):
    rev = 0
    tmp = n
    while n != 0:
        rev = rev * 10 + n%10
        n //= 10
    return tmp == rev
def chinhphuong(n):
    can = isqrt(n)
    return can*can == n
def check(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return snt(tong)
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt1,cnt2,cnt3,cnt4 = 0,0,0,0
    for x in a:
        if snt(x):
            cnt1 += 1
        if chinhphuong(x):
            cnt3 += 1
        if tn(x):
            cnt2 += 1
        if check(x):
            cnt4 += 1
    print(cnt1, cnt2, cnt3, cnt4, sep = '\n')
        
        