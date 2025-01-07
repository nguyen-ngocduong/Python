from math import *
def scp(n) :
    can = isqrt(n)
    if n == can*can:
        return 1
    return 0
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        if(scp(n)) :
            print("YES")
        else:
            print("NO")
    print()