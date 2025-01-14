#Cặp số có tổng lớn hơn k
def ham1(a, l, r,x):
    res = -1
    while l <= r:
        m = (l+r)//2
        if a[m] > x:
            res = m
            r = m - 1
        else :
            l = m + 1
    return res

if __name__ == '__main__':
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n): # tìm [i+1, n - 1] > k - a[i]
        p1 = ham1(a, i+1, n-1, k - a[i])
        if p1 != -1:
            ans += n- p1
    print(ans)