#truy vấn trên mảng
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else :
            d[x] = 1
    q = int(input())
    for _ in range(q):
        t,x = map(int, input().split())
        if t == 1:
            if x in d:
                d[x] += 1
            else: d[x] = 1
        elif t == 2:
            if x in d:
                d[x] -= 1
                if d[x] == 0:
                    d.pop(x)
        else:
            if x in d:
                print('YES')
            else:
                print('NO')