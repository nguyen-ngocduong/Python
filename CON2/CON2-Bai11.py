tc = int(input())
for _ in range(tc) :
    a,b,c = map(int, input().split())
    if a > 0 and  b > 0 and c > 0 and a+b > c and b+c > a and c+a > b:
        if a == b and b == c:
            print("1")
        elif a == b or b == c or a == c:
            print("2")
        elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2 :
            print("3")
        else: print("4")
    else : print("INVALID")