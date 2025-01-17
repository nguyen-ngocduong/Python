#Ma trận xoáy ốc fibonacci
fibo = [0]*100
def init():
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2,100):
        fibo[i] = fibo[i-1] + fibo[i-2]
if __name__ == '__main__':
    init()
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    c1, c2, h1, h2 = 0, n - 1, 0, n - 1
    tmp = 0
    while tmp < n*n:
        # xay dung hang 1
        for i in range(c1, c2 + 1):
            a[h1][i] = fibo[tmp]
            tmp += 1
        h1 += 1
        # Xay dung cot 2
        for i in range(h1, h2 + 1):
            a[i][c2] = fibo[tmp]
            tmp += 1
        c2 -= 1
        # Xay dung hang 2
        for i in range(c2, c1 - 1, -1):
            a[h2][i] = fibo[tmp]
            tmp += 1
        h2 -= 1
        # Xay dung cot 1
        for i in range(h2, h1 - 1, -1):
            a[i][c1] = fibo[tmp]
            tmp += 1
        c1 += 1
    for i in range(n):
        for j in range(n):
            print(a[i][j],end = ' ')
        print()