#Lớn hơn liền kề
from math import *
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            print(a[i], end = ' ')
            