from math import *

def is_sphenic(n):
    cnt = 0
    step = 1  
    i = 2
    while i*i <= n:
        
        if n % i == 0:
            d = 0
            cnt += 1
            while n % i == 0:
                d += 1
                n //= i
                if d > 1:
                    return False
        if i >= 3:
            i += 2
        else:
            i += 1
          
    if n != 1:
        cnt += 1
    return cnt == 3

if __name__ == "__main__":
    n = int(input())
    if is_sphenic(n):
        print(1)
    else:
        print(0)