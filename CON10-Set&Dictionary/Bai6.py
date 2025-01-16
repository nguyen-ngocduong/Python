#Intersection
if __name__ == '__main__':
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s1 = set(a)
    s2 = set(b)
    s3 = list(s1.intersection(s2))
    for x in a:
        if x in s3:
            print(x, end = ' ')
            s3.remove(x)