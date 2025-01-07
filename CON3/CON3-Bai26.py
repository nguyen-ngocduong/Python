tc = int(input())
for _ in range(tc):
    a,b,n = map(int, input().split())
    check = False
    for x in range(0, n//a + 1):
        tmp = n - a * x
        if tmp % b == 0 :
            check = True
            break
    if check:
        print("YES")
    else : print("NO")

    