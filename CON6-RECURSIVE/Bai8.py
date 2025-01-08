def DectoBin(n):
    if n!=0:
        DectoBin(n // 2)
        print(n%2, end = '')
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        if n == 0:
            print(0)
        else : DectoBin(n)
        print()