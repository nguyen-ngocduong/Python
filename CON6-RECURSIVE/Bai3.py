def tong1(n):
    if n == 0:
        return 0
    return n+tong1(n-1)
def tong2(n):
    if n == 0:
        return 0
    return n**2 + tong2(n-1)
def tong3(n):
    if n == 0:
        return 0
    return n**3 + tong3(n-1)
def tong4(n):
    if n == 1:
        return -1
    return (-1)**n * n + tong4(n-1)
def giaithua(n):
    if n == 0:
        return 1
    return n*giaithua(n-1)
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(tong1(n))
        print(tong2(n))
        print(tong3(n))
        print(tong4(n))
        print(giaithua(n))