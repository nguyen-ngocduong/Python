#tính tổng và tích các phần tử
MOD = 10**9 + 7
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    tong = sum(a)
    tich = 1
    for i in range(len(a)):
        tich *= a[i]
    print(tong % MOD, tich % MOD, sep = '\n', end = '')