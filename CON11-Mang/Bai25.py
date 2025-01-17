#Diện tích # chung cạnh => path 4
a = []
dem = 0 # lưu diện tích vùng chứa i,j
n,m = 0,0
path = [[-1,0], [0,-1], [1,0],[0,1]]
def loang(i,j):
    a[i][j] = 0
    global dem
    dem += 1
    for x, y in path :
        i1 = i + x
        j1 = j + y
        if 0 <= i1 < n and 0 <= j1 < m and a[i1][j1] == 1:
            loang(i1,j1)
if __name__ == '__main__':
    n, m = map(int, input().split())
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                dem = 0
                loang(i,j)
                ans = max(ans, dem)
    print(ans)