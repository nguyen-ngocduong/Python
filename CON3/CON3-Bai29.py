tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for x in a:
        if x%2 == 0:
            sum += x
    print(sum)