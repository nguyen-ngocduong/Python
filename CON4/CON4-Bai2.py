from math import *
def prime (n) :
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0 :
            cnt += 1
    if cnt == 2 :
        return True
    else : return False
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        if prime(n) :
            print("YES")
        else : print("NO")
    print()