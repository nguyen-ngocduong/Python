#Phần tử riêng biệt
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for key in d.items():
        print(key[0], end = ' ')