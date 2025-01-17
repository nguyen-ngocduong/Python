#Maximum path sum: tìm đường đi [1,1] -> [n,m] | chi phí max
if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    f = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                f[0][0] = a[0][0]
            elif i == 0:
                f[i][j] = f[i][j-1] + a[i][j]
            elif j == 0:
                f[i][j] = f[i-1][j] + a[i][j]
            else:
                f[i][j] = max(f[i-1][j],f[i][j-1]) + a[i][j]
    print(f[n-1][m-1])