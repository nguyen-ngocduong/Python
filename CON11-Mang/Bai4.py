def tn(n):
    tmp = n
    rev = 0
    while n!=0:
        rev = rev*10 + n % 10
        n //= 10
    return tmp == rev
if __name__ == '__main__':
    n=int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    dem = 0
    for i in range(n):
        for j in range(i+1):
            if tn(a[i][j]):
                dem += 1
    print(dem)