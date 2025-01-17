#Số điểm cực đại
n,m = 0,0
a = []
path = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def check(i,j):
    for x, y in path:
        i1 = i + x
        j1 = j + y
        if 0<=i1<n and 0<=j1<m :
            if a[i1][j1] >= a[i][j]:
                return False
    return True
if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    dem = 0
    for i in range(n):
        for j in range(m):
            #ktra a[i][j] có p là điểm cực đại ko
            if check(i,j):
                dem += 1
    print(dem)