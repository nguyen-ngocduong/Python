tc = int(input())
for _ in range(tc) :
    a,b = map(int, input().split())
    if a >= 1 and a <= 12 and b > 0:
        if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
            print("31",b)
        elif a == 2 :
            if b%400 == 0 or (b%4 == 0 and b%100 != 0):
                print("29", b)
            else : print ("28", b)
        else : print("30", b)
    else: print("INVALID")