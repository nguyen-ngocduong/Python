from math import *
def prime(n):
    if n == 1 or n == 0 :
        return 0
    for i in range(2, isqrt(n)+1):
        if n % i == 0 :
            return 0
    return 1

def thuanprime(n):
    tong = 0
    while n != 0:
        tmp = n % 10
        if tmp not in (2, 3, 5, 7):  # Kiểm tra nếu chữ số không phải là số nguyên tố
            return False
        tong += tmp
        n //= 10
    return prime(tong)

if __name__ == "__main__" :
    tc = int(input())
    for _ in range(tc):
        a,b = map(int, input().split())
        dem = 0
        for i in range(a, b+1) :
            if thuanprime(i) and prime(i):
                dem += 1
        print(dem)
    print() 