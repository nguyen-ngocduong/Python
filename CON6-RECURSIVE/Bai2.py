#số fibonacci
MOD = 10**9 + 7
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))%MOD
def gcl(a,b) :
    if b == 0:
        return a
    return gcl(b, a%b)
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n,m = map(int, input().split())
        print(fibo(n))
        print(gcl(n,m))