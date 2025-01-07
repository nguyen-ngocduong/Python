tc = int(input())
for _ in range(tc):
    n = int(input())
    if n < 2:
        print(-1)
        print()
    elif n % 2 == 0:
        print(n//2)
        for i in range(1, n//2 +1):
            print(2, end = " ")
        print()
    else :
        print(n//2)
        for i in range(1, n//2 - 1):
            print(2, end = ' ')
        print(3)