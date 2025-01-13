#Tìm gcd của mọi ptu trong mảng
from math import *
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    for i in range(len(a)):
        ans = gcd(ans, a[i])
    print(ans)