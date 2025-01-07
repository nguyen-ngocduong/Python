#So chinh phuong 3
from math import *
def scp(n):
    can = isqrt(n)
    if can*can == n :
        return 1
    return 0
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        a,b = map(int, input().split())
        dem = 0
        can1, can2 = isqrt(a), isqrt(b)
        if can1 * can1 != a:
            can1 += 1
        if (can2 + 1)*(can2 + 1) != b :
            can2 += 1
        for i in range(can1,can2+1):
            dem += 1
        print(dem)
    print()