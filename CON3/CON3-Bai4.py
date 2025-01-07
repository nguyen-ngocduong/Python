tc = int(input())
for _ in range(tc):
    n = int(input())
    tong = 0
    for i in range(1,n+1):
        if(i%3 == 0):
            tong += i
    print(tong)