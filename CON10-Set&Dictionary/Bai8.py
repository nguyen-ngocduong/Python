#Symmetric difference
if __name__ == '__main__':
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s1 = set(a)
    s2 = set(b)
    s3 = list(s1.symmetric_difference(s2))
    s3.sort()
    for x in s3: 
        print(x, end = ' ')