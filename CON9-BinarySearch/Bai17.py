#Đèn lồng
if __name__ == '__main__':
    n,l = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = max(a[0]-0, l - a[n-1])
    for i in range(1,n):
        ans = max(ans, (a[i]-a[i-1])/2)
    print('%.10f' % ans)