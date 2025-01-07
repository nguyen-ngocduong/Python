n = int(input())
dem = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        dem += 1
        print(dem, end = ' ')
    print()
print()
for i in range(1, n+1):
    cnt = i
    for j in range(1, n+1):
        print(cnt, end = ' ')
        cnt += 1
    print()
print()
for i in range(1, n+1):
    for j in range(1,n+1):
        if j <= n-i:
            print("~", end = '')
        else :
            print(i, end = '')
    print()
print()
for i in range(1, n+1):
    init = i
    kh = n-1
    for j in range(i):
        print(init, end = ' ')
        init += kh
        kh -= 1
    print()
print()