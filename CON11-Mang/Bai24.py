#Phần tử xuất hiện ở mọi hàng
if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    cnt = [0]*105
    for i in range(n):
        for j in range(n):
            if i == 0:
                cnt[a[i][j]] = 1
            else:
                if cnt[a[i][j]] == i:
                    cnt[a[i][j]] = i + 1
    check = False                    
    for i in range(101):
        if cnt[i] == n:
            print(i, end = ' ')
            check = True
    if not check:
        print("NOT FOUND")