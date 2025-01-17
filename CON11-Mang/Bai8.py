#Hoán vị 2 côt
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    x, y = map(int, input().split())
    x,y = x-1, y-1
    for i in range(n):
        a[i][x], a[i][y] = a[i][n-x-1], a[i][n-y-1]
        for j in range(n):
            print(a[i][j], end = ' ')
        print()