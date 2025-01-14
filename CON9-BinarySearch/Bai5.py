#Số xuất hiện nhiều nhất trong mảng
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    res = 1
    a.append(10**18)
    ans = a[0]
    for i in range(1,len(a)):
        if a[i] == a[i-1]:
            cnt += 1
        else:
            if cnt > res:
                res = cnt
                ans = a[i-1]
            cnt = 1
    print(ans, res)