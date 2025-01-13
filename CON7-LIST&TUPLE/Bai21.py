#Đếm phân phối sử dụng mảng
from math import *
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0]*1001
    for x in a:
        cnt[x] += 1
    for x in a:
        if cnt[x] != 0:
            print(x, cnt[x], end = ' ')
            cnt[x] = 0
            print()
    b = sorted(a)
    cnt2 = [0]*1001
    for x in b:
        cnt2[x] += 1
    for x in b:
        if cnt2[x] != 0:
            print(x, cnt2[x], end = ' ')
            cnt2[x] = 0
            print()
    l,r = min(a), max(a)
    cnt3 = cnt.copy()
    for i in range(l, r+1):
        if cnt3[i] != 0:
            print(i, cnt3[i])
    max_fre, max_val = 0,0
    for i in range(l,r+1):
        if cnt3[i] >= max_fre:
            max_fre = cnt3[i]
            max_val = i
    print( max_val, max_fre)