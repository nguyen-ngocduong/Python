#Liệt kê các giá trị khác nhau
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0]*1001
    for x in a:
        if cnt[x] == 0:
            print(x, end = ' ')
            cnt[x] = 1
            