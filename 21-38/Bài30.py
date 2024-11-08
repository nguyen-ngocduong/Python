h = int(input("Nhập chiều cao h: "))
for i in range(h) :
    if i == 0 :
        print("*" * h)
    elif i < h-1 :
        print("*" * (h-i))
    else :
        print("*")         