#Đếm các phần tử là snt trên đường chéo chính và đường chéo phụ
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
    dem = 0
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    for i in range(n):
        #a[i][i]: ptu đường chéo chính, a[i][n-i-1] : đường chéo phụ
        if snt(a[i][i]):
            dem += 1
        if snt(a[i][n-i-1]):
            dem += 1
    if n % 2 == 1:
        if snt(a[n//2][n//2]):
            dem -= 1
    print(dem)