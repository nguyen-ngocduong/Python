#Các số khác nhau trong mảng
if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 1
    a.sort()
    for i in range(1,n):
        if a[i] != a[i-1]:
            cnt += 1
    print(cnt)