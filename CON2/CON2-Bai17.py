tc = int(input())
for _ in range(tc) :
    c = input()
    tmp = ord(c)
    if tmp >= 65 and tmp <= 90:
        print("UPPER")
    elif tmp >= 97 and tmp <= 122:
        print("LOWER")
    elif tmp >= 48 and tmp <= 57:
        print("DIGIT")
    else:
        print("SPECIAL")