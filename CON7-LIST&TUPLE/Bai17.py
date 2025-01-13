#Mảng đối xứng
from math import *
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for x in a:
        b.append(x)
    b.reverse()
    if a == b:
        print("YES")
    else:
        print("NO")