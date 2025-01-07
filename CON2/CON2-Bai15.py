tc = int(input())
for _ in range(tc) :
    n,a,b = map(int, input().split())
    if a <= b/2 :
        print(n*a)
    else:
        if n % 2 == 0:
            print(n // 2 * b)
        else:
            print((n-1)//2 * b + a)