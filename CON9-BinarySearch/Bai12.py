#Cặp số có tổng bằng k
def ham2(a,l,r,x): #ptu cuoi lớn hơn k
    res = -1
    while l <= r:
        m = (l+r) //2
        if a[m] == x:
            res = m
            l = m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res
def ham1(a,l,r,x): #ptu đầu tiên lớn hơn k
    res = -1
    while l <= r:
        m = (l+r) // 2
        if a[m] == x:
            res = m
            r = m -1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res
if __name__ == '__main__':
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        #tìm [i + 1, n - 1] => k - a[i]
        p1,p2 = ham1(a, i+1, n-1, m-a[i]), ham2(a,i+1,n-1,m-a[i])
        if p1 != -1:
            ans += p2 - p1 + 1
    print(ans)