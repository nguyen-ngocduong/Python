#so loc phat
def check(n):
    while n != 0:
        tmp = n%10
        if tmp != 6 and tmp != 8 and tmp != 0 :
            return 0
        n //= 10
    return 1
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        if check(n) :
            print("YES")
        else:
            print("NO")
    print()