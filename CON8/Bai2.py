#Fibonacci
fibo = [0]*(10**6+1)
MOD = 10**7 + 1
def init():
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, 1000001):
        fibo[i] = fibo[i-1] + fibo[i-2]
        fibo[i] = fibo[i] % MOD

if __name__ == '__main__':
    init()
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(fibo[n])