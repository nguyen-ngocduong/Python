#đếm các phần tử là snt trên đường chéo chính và phụ 2
from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n%i ==0:
            return False
    return True
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    s = set({})
    dem = 0
    for i in range(n):
        for j in range(n):
            if snt(a[i][i]):
                s.add(a[i][i])
            elif snt(a[i][n-i-1]):
                s.add(a[i][n-i-1])
    dem = len(s)
    print(s)
    print(dem)