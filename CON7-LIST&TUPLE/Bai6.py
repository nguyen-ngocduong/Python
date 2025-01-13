#Cặp số 1
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    dem = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == k :
                dem += 1
    print(dem)