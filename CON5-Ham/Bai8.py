#so co so luong uoc la so le
from math import *
def scp(n):
    can = isqrt(n)
    if can*can == n :
        return 1
    return 0
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        if(scp(n)):
            print("YES")
        else:
            print("NO")
    print()