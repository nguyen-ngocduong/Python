#Khiêu vũ
if __name__ == '__main__':
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i,j = 0,0
    dem = 0
    while i < n and j < m:
        if a[i] > b[j] :
            dem += 1
            i += 1
            j += 1
        else: # tăng chiều cao của nam
            i += 1
    print(dem)