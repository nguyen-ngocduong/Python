#Tổng hàng tổng cột
if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    # tính tổng từng hàng
    tong1 = [sum(row) for row in a]
    for x in tong1:
        print(x)
    print()
    for j in range(m):
        tong2 = 0
        for i in range(n):
            tong2 += a[i][j]
        print(tong2)