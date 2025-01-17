#In ra ma trận theo mẫu
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    print('Pattern 1:', end ='\n')
    for i in range(n):
        for j in range(n):
            print(a[j][i], end = ' ')
        print()
    print('Patern 2: ', end = '\n')
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            print(a[i][j], end = ' ')
        print()
    print('Patern 3: ', end = '\n')
    for i in range(n-1, -1, -1):
        for j in range(n):
            print(a[j][i], end = ' ')
        print()
    print('Patern 4: ', end = '\n')
    for i in range(n):
        for j in range(n-1,-1,-1):
            print(a[i][j], end = ' ')
        print()
