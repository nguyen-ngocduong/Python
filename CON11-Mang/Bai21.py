#Đường đi quân mã
path = [[-2,-1], [-2,1], [-1,-2], [-1,2],[1,-2],[1,2],[2,-1],[2,1]]
n,m=0,0
a = []
def loang(i,j) :
    a[i][j] = 0
    for x,y in path:
        i1 = x + i
        j1 = y + j
        if 0<=i1<n and 0<=j1<m and a[i1][j1] == 1:
            loang(i1,j1)
if __name__ == '__main__':
    n, m = map(int, input().split())
    s,t,u,v = map(int, input().split())
    s,t,u,v = s-1,t-1,u-1,v-1
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    loang(s,t)
    if a[u][v] == 0:
        print("YES")
    else:
        print("NO")