#Giai thừa dư
F = [0]*(10**6+1)
MOD = 10**7 + 1
def init():
    F[0] = 1
    for i in range(1, 10**6 + 1):
        F[i] = F[i-1] * i
        F[i] = F[i] % MOD
if __name__ == '__main__':
    init()
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(F[n])