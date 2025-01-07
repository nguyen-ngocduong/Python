tc = int(input())
for _ in range(tc) :
    a,b,c,d = map(float, input().split())
    mean = (a + b + c*2 + d*3) / 7
    if mean >= 8:
        print("GIOI")
    elif mean >= 6.5 and mean < 8:
        print("KHA")
    elif mean >= 5 and mean < 6.5:
        print("TB")
    else : print("YEU")