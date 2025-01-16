#union
if __name__ == '__main__':
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s1 = set(a)
    s2 = set(b)
    s3 = sorted(list(s1.union(s2)), reverse=True)
    for x in s3:
        print(x, end = ' ')