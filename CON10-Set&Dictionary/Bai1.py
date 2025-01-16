#phần tử phân biệt
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    d = {}
    print(len(b))
    for x in a:
        d[x] = 1
    print(d, len(d))