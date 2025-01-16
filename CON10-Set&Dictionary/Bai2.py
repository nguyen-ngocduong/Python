#truy vấn phần tử trong mảng
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # a = set(a)
    # q = int(input())
    # for _ in range(q):
    #     x = int(input())
    #     if x in a:
    #         print("YES")
    #     else:
    #         print("NO")
    #c2: sử dụng dict
    d = {}
    for x in a:
        d[x] = 1
    q = int(input())
    for _ in range(q):
        x = int(input())
        if x in d :
            print("YES")
        else:
            print("NO")