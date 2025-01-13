"""Input:
   6
   3 8 4 9 12 27
   3
   Output:
   15 21 25 48"""
from math import *
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    for i in range(0,n-k+1):
        tong = 0
        for j in range(i, i+k):
            tong += a[j]
        print(tong)