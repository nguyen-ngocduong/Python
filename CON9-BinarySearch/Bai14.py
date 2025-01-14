#Cặp số có tổng nhỏ hơn k
def ham1(a, l, r, x): # tìm vị trí cuối cùng của ptu nhỏ hơn k
    res = -1
    while l <= r:
        mid = (l+r) // 2
        if a[mid] < x:
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res 
if __name__ == '__main__':
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n):
        #tìm [i+1, n-1] => k - a[i]
        p1 = ham1(a, i + 1, n - 1, k - a[i])
        if p1 != -1:
            res += p1 - i
    print(res)