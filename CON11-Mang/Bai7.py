#Hoán vị 2 hàng của ma trận
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    x, y = map(int, input().split())
    x,y = x-1, y-1
    for i in range(n):
        a[x][i], a[y][i] = a[y][i],a[x][i]
        for j in range(n):
            print(a[i][j], end = ' ')
        print()