from math import *
def dem_uoc(n):
    cnt = 0
    for i in range(1, isqrt(n) + 1):
        if n%i == 0:
            cnt += 1
            if i != n//i :
                cnt += 1
    return cnt
def tong_uoc(n):
    tong = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n//i
    return tong
if __name__ == '__main__' :
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(dem_uoc(n))
        print(tong_uoc(n))
    print()