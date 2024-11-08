n = int(input("Nhập số lần: "))
x = 0
while x < n :
    a = int(input())
    x += 1
    if a > 1 :
        for i in range (2,int(a**0.5)+1) :
            if a % i == 0 :
                print("No")
                break
        else:
            print("Yes")
    else :
        print("No")
        



