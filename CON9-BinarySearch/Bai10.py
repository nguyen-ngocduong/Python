#Xếp gạch
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dem = 1
    docung = a[0]
    for i in range(1, n):
        if docung <= 0:
            break
        else:
            dem += 1
        docung = min(docung - 1, a[i])
    print(dem)
        