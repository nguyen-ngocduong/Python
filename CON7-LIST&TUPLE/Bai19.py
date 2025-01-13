#Khác biệt nhỏ nhất
from math import *
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    min_dis = 10**6+1
    for i in range(len(a)):
        for j in range(i+1, n):
            min_dis = min(min_dis, abs(a[i] - a[j]))
    print(min_dis)