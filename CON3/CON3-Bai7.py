from math import *
n = int(input())
tong = 0
for i in range(1, isqrt(n)+1):
    if n%i == 0:
        tong += i
        if i != n//i :
            tong += n//i
print(tong)