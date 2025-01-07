#phân tích thừa số nguyên tố
from math import *
def ptichPrime(n):
    for i in range(2, isqrt(n)):
        if n%i == 0:
            while n % i == 0 :
                print(i, end = ' ')
                n //= i
    if n >1 :
        print(n)
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        ptichPrime(n)
    print()