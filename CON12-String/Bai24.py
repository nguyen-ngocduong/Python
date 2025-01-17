#Xâu đầu cuối giống nhau
#(đếm số lượng xâu con mà có đầu cuối giống nhau)
from math import comb
if __name__ =='__main__':
    s = input()
    cnt = [0]*256
    for x in s:
        cnt[ord(x)] += 1
    ans = len(s)
    for i in range(256):
        if cnt[i] != 0:
            ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)