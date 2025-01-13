#Cặp số 2
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    min_val = 10**9
    for i in range(n):
        for j in range(i+1, n):
            if abs(a[j] - a[i]) < min_val:
                min_val = abs(a[j] - a[i])
    print(min_val)