#lớn hơn, nhỏ hơn
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    lon, nho = 0,0
    for i in a:
        if i >= x :
            lon += 1
        else:
            nho += 1
    print(nho, lon, sep = '\n')