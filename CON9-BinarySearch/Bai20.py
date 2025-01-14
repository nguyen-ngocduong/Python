#Biểu thức nhỏ nhất
if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a[1:] = sorted(a[1:], reverse=True)
    res = a[0]
    for i in range(1, n):
        if i <= k:
            res += a[i]
        else :
            res -= a[i]
    print(res)