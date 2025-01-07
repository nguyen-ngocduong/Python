#tim uoc ngto lon nhat
from math import *
def solve(n):
    ans = -1
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            ans = i
            while  n%i == 0:
                n //= i
    if n > 1:
        ans = n
    return ans
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(solve(n))
