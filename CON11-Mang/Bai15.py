#Nhân 2 ma trận
if __name__ == '__main__':
    n, m, p = map(int, input().split())
    a, b = [], []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp)
    for i in range(m):
        tmp = list(map(int, input().split()))
        b.append(tmp)
    ans = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                ans[i][j] += a[i][k] * b[k][j]
    for i in range(n):
        for j in range(p):
            print(ans[i][j], end = ' ')
        print()