#Snake
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                print(a[i][j], end = ' ')
        else:
            for j in range(n-1, -1, -1) :
                print(a[i][j], end = ' ')
        print()
        