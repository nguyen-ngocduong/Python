def tong(n):
    if n < 10:
        return n
    else :
        return n % 10 + tong(n // 10)
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(tong(n))
    print()