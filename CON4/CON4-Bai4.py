#số chính phương
from math import *
def scp(n) :
    can = isqrt(n)
    if can*can == n :
        return True
    else : 
        return False
if __name__ == '__main__':
    n = int(input())
    if(scp(n)) :
        print("YES")
    else: print("NO")