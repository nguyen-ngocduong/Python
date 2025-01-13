#Cân bằng nguyên tố
from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    x = sum(a)
    for i in range(1, n-1):
        tmp = x - a[i]
        res = 0
        for j in range(0,i):
            res += a[j]
        if snt(res) and snt(tmp - res):
            print(i, end = ' ')
