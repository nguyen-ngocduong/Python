#Count island 1 (chung cạnh)
n,m = 0,0
a = []
path = [[-1,0],[0,-1],[0,1],[1,0]]
def loang(i, j):
    a[i][j] = 0  # Đánh dấu ô đã duyệt
    for x, y in path:
        i1, j1 = i + x, j + y
        # Kiểm tra biên và ô có giá trị 1 (nước)
        if 0 <= i1 < n and 0 <= j1 < m and a[i1][j1] == 1:
            loang(i1, j1)
if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    dem = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                dem += 1
                loang(i,j)
    print(dem)