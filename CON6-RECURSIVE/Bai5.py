#UCLN,BCNN
def _gcd(a,b):
    if b == 0:
        return a
    return _gcd(b, a%b)
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        a,b = map(int, input().split())
        print(_gcd(a,b), a*b // _gcd(a,b))
    print()