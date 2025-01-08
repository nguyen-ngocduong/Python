#DectoHex
def DectoHex(n):
    if n != 0:
        DectoHex(n // 16)
        tmp = n % 16
        if tmp < 10 :
            print(tmp, end = '')
        else:
            print(chr(tmp+55), end = '')
if __name__ == "__main__" :
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        if n == 0:
            print(0)
        else: DectoHex(n)
        print()