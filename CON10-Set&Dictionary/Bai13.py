#Hợp và giao mảng 2
if __name__ == '__main__':
    n,m = map(int,input().split())
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))
    c = list(a.intersection(b))
    d = list(a.union(b))
    for x in d:
        print(x, end = ' ')
    print()
    for x in c:
        print(x, end = ' ')