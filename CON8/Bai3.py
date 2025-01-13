#Tribonacci
#Fibonacci
tribo = [0]*(10**6+1)
MOD = 10**7 + 1
def init():
    tribo[0] = 0
    tribo[1] = 0
    tribo[2] = 1
    for i in range(3, 1000001):
        tribo[i] = tribo[i-1] + tribo[i-2] + tribo[i - 3]
        tribo[i] = tribo[i] % MOD

if __name__ == '__main__':
    init()
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(tribo[n])