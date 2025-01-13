#Cửa sổ cỡ k
from math import *
if __name__ == '__main__':
    n,k = map(int,input().split())
    a = list(map(int, input().split()))
    for i in range(0, n-k+1):
        print(sum(a[i:i+k]), end = ' ')