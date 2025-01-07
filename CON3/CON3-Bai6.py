tc = int(input())
for _ in range(tc) :
    n = int(input())
    tong = 0
    for i in range(1,n+1):
        tong += float(0.5 * 1/i)
    print("%.5f" % tong)