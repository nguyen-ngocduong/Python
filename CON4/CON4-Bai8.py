from math import *
def prime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return 0
    return 1
def tongchuso(n):
    sum = 0
    while n != 0:
        sum += n%10
        n //= 10
    return sum
def tongchan(n):
    sum = 0
    while n != 0:
        if n % 10 %2 ==0:
            sum += n%10
        n //= 10
    return sum
def ham4(n):
    sum = 0
    while n!=0:
        tmp = n % 10
        if tmp == 2 or tmp == 3 or tmp == 5 or tmp == 7 :
            sum += tmp
        n //= 10
    return sum
def ham5(n): # đảo ngược
    rev = 0
    while n!= 0:
        rev = rev * 10 + n%10
        n //= 10
    return rev
def ham6(n) : # đếm số lượng ước nguyên tố của n
    count = 0
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    if n > 1 :
        count += 1
    return count
def ham7(n):
    res = -1
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            res = i #gặp thừa số nguyên tố nào thì gán vào kq
            while n % i == 0:
                n //= i
    if n > 1: 
        res = n
    return res
def ham8(n):
    while n!=0:
        if n%10 == 6:
            return 1
        n //= 10
    return 0
def ham9(n) :
    tong = 0
    while n!=0:
        tong += n % 10
        n //= 10
    if tong % 8 == 0:
        return 1
    return 0
def ham10(n): # tổng giai thừa
    tong = 0
    while n != 0:
        tong += factorial(n%10)
        n //= 10
    return tong
def ham11(n):
    du = n%10
    while n != 0:
        if du != n %10 :
            return 0
        n //= 10
    return 1
def ham12(n) :
    dvi = n %10
    while n != 0:
        if n%10 > dvi:
            return 0
        n //= 10
    return 1
def ham13(n) :
    m = n
    dem = 0
    while n != 0:
        dem +=1 
        n //= 10
    tong = 0
    while m != 0:
        tong += pow(m%10, dem)
        m //=10
    return tong
if __name__ == '__main__' :
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(prime(n))
        print(tongchan(n))
        print(tongchuso(n))
        print(ham4(n))
        print(ham5(n))
        print(ham6(n))
        print(ham7(n))
        print(ham8(n))
        print(ham9(n))
        print(ham10(n))
        print(ham11(n))
        print(ham12(n))
        print(ham13(n))
