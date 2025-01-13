#mảng cộng dồn
from math import *
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    F = [0] * n
    for i in range(len(a)):
        F[i] = a[i] + F[i-1]
    for x in F:
        print(x, end = ' ')