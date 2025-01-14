#Khoảng cách nhỏ nhất
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    res = 10**18
    for i in range(1,n):
        res = min(res, a[i] - a[i-1])
    print(res)