def giaithua(n):
    if n == 0 :
        return 1
    else:
        return n*giaithua(n-1)
tc = int(input())
for _ in range(tc):
    n = int(input())
    res = 0
    for i in range(n):
        res += 1/giaithua(i)
    print("%.4f" % res)
print()