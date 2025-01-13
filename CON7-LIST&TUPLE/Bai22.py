#Xóa
from math import *
if __name__ == '__main__':
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    if x in a:
        a.remove(x)
        for i in range(len(a)):
            print(a[i], end = ' ')
    else:
        print("NONE")