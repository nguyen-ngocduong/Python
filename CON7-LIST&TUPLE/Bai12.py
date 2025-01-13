#vị trí số lớn nhất, snn
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    x = max(a)
    y = min(a)
    for i in range(n-1,-1,-1):
        if a[i] == x:
            print(i, end = ' ')
            break
    for i in range(len(a)):
        if a[i] == y:
            print(i)
            break