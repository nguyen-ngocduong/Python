#Liệt kê và đếm
from sys import stdin
def check(n):
    tmp = n%10
    while n!=0:
        if tmp < n%10:
            return False
        n //= 10
    return True
if __name__ == '__main__':
    d = {}
    for line in stdin:
        a = list(map(int, line.split()))
        for x in a:
            if x in d:
                d[x] += 1
            else: d[x] = 1
        d = list(d.items())
        b = sorted(d, key=lambda x: (x[1], x[0]), reverse=True)
        for val, fre in b:
            if check(val):
                print(val, fre)
