tc = int(input())
for _ in range(tc):
    a,b,c = map(int, input().split())
    if (a+b > c) and (b+c > a) and (c + a > b) :
        print("YES")
    else : print("NO")