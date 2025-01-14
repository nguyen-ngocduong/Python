#Dragon
if __name__ == '__main__':
    n,s = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    a.sort(key=lambda x : x[0]) # sắp xếp theo sức mạnh tăng dần
    for x, y in a:
        if x >= s:
            print('NO')
            exit()
        s += y
    print('YES')