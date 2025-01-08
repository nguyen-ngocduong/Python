#lũy thừa nhị phân
MOD = 10**9+7
def power(a,b):
    if b == 0: 
        return 1
    tmp = power(a,b//2)
    if b % 2 == 1:
        return tmp * tmp * a % MOD
    else: 
        return tmp*tmp % MOD
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        a,b = map(int, input().split())
        print(power(a,b))
    print()