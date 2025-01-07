#so chinh phuowng trong doan
from math import *
def scp(n):
    can = isqrt(n)
    if n == can*can:
        return 1
    return 0
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        a,b = map(int, input().split())
        can1,can2 = isqrt(a), isqrt(b)
        if can1 * can1 != a:
            can1 += 1
        for i in range(min(can1,can2), max(can1,can2)+1):
            print(i*i, end = ' ')
        print()