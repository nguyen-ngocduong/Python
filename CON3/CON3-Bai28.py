tc = int(input())
for _ in range(tc):
    n = int(input())
    tmp = 1
    res = 0
    for i in range(1, n+1):
        tmp *= i
        res += tmp
    print(res)