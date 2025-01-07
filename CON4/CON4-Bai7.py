# Kiểm tra số fibo, in ra số fibo thứ n, in ra số fibo thứ 1...
from math import *
def fibo(n) :
    print('0 1', end = ' ')
    fn1, fn2 = 1,0
    for i in range(2,n):
        fn = fn1 + fn2
        print(fn, end = ' ')
        fn2, fn1 = fn1, fn
def checkfibo(n):
    if n == 0 or n == 1:
        return True
    fn1 = 1 
    fn2 = 0
    for i in range(2,n):
        fn = fn1 + fn2
        if fn == n:
            return True
        fn2, fn1 = fn1, fn
    return False

def printfibo(n):
    if n == 0 or n == 1:
        print(n)
    fn1,fn2 = 1,0
    for i in range(1,n+1):
        fn = fn1 + fn2
        fn2,fn1 = fn1,fn
    print(fn)
if __name__ == '__main__':
    fibo(10)
    print()
    n = int(input())
    if checkfibo(n) :
        print("YES")
    else : print("NO")
    print(printfibo(n))