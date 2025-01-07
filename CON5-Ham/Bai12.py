#so thuan nghich, loc phat
def check(n):
    tmp = n
    tong = 0
    rev = 0
    ok = False
    while n != 0:
        rev = rev * 10 + n % 10
        if n % 10 == 6 :
            ok = True
        tong += n%10
        n //= 10
    return (rev == tmp) and (tong % 10 == 8) and ok
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            if(check(i)):
                print(i, end = ' ')
        print()