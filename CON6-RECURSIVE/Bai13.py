#In ra số nguyên
def nguoc(n):
    if n < 10:
        print(n, end = ' ')
    else:
        print(n%10, end = ' ')
        nguoc(n//10)
def xuoi(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    nguoc(rev)

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        nguoc(n)
        print()
        xuoi(n)
    print()