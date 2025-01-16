#Suffix and Query
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        l = int(input())
        s = set(a[l:])
        print(len(s))