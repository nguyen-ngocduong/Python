#Sắp xếp trẻ
if __name__ == '__main__':
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dem = 0
    l,r = 0, n-1
    while l <= r:
        if a[l] + a[r] <= x:
            dem += 1
            l += 1
            r -= 1
        else:
            dem += 1
            r -= 1
    print(dem)