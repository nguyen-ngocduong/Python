tc = int(input())
for _ in range(tc):
    n,m,a = map(int, input().split())
    if n%a == 0 and m%a == 0 :
        print((n//a)*(m//a))
    else :
        print((n//a + 1) * (m//a + 1))