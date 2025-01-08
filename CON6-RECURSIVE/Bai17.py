#đếm số thao tác
def count(n):
    if n == 1:
        return 0
    tmp1, tmp2, tmp3 = 10**9, 10**9, 10**9
    if n % 2 == 0:
        tmp1 = 1 + count(n // 2)
    if n % 3 == 0:
        tmp2 = 1 + count(n//3)
    if n > 1:
        tmp3 = 1 + count(n-1)
    return min(tmp1, tmp2, tmp3)
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(count(n))
    print()