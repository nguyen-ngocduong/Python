#Vắt sữa bò
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    ans = 0 # lưu sản lượng
    for i in range(n):
        #a[i] mất i lít sữa
        if a[i] - i > 0:
            ans += a[i] - i
        else:
            break
    print(ans)