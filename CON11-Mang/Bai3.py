#Số lớn nhất, số nhỏ nhất trong ma trận
if __name__ == '__main__':
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    min_val, max_val = 10**18, -10**18
    for i in range(n):
        for j in range(n):
            min_val = min(min_val, a[i][j])
            max_val = max(max_val, a[i][j])
    print(min_val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == min_val:
                print(i+1,j+1)
    print(max_val)       
    for i in range(n):
        for j in range(m):
            if a[i][j] == max_val:
                print(i+1,j+1)