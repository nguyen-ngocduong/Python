h = int(input("Nhập chiều cao h : "))
for i in range (h) :
    if i == 0:
        print("*")
    elif i < h-1 :
        print("*"*(i+1))
    else :
        print("*"*h)    