#tìm hợp và giao của 2 mảng 1
#Đếm tần suất
from collections import Counter
if __name__ == '__main__':
    n,m = map(int, input().split())
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))
    c = list(a.intersection(b))
    d = list(a.union(b))
    c.sort()
    d.sort()
    for x in c:
        print(x, end=' ')
    print()
    for x in d:
        print(x, end = ' ')
