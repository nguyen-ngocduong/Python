#Điền số còn thiếu
# if __name__ == '__main__':
#     n = int(input())
#     a = list(map(int, input().split()))
#     l,r = min(a), max(a)
#     cnt = [0]*(10**6 + 1)
#     ans = 0
#     for x in a:
#         cnt[x] = 1
#     for i in range(l, r + 1):
#         if cnt[i] == 0:
#             ans += 1
#     print(ans)
#c2

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1,n):
        kc = a[i] - a[i-1]
        if kc > 1:
            ans += kc - 1  # Tính khoảng cách cần thu hẹp
    print(ans)
        