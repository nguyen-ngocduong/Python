#trung bình cộng nguyên tố
from math import *
def prime(n):
    if n < 2 :
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    tong,dem = 0,0
    for x in a:
        if prime(x):
            dem += 1
            tong += x
    print('%2.f' % (tong / dem))