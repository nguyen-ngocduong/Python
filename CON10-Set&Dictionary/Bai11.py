#Đếm tần suất
from collections import Counter
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    b = list(dict(Counter(a)).items())
    c = sorted(b, key = lambda x : x[0])
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    for val, fre in c:
        print(val, fre)
    print()
    for key, val in d.items():
        print(key, val, sep = ' ', end = '\n')