#Sắp xếp theo cột
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    columns = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n) :
        for j in range(n):
            columns[i][j] = a[j][i]
    for i in range(n):
        columns[i].sort()
    # in theo cột của ma trận columns
    for i in range(n):
        for j in range(n):
            print(columns[j][i], end=' ')
        print()