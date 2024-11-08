h = int(input("Nhập chiều cao h: "))
for i in range (h):
    if i == 0 or i == h-1 :
        print("*"*h)
    else :
        print("*" + " " * (h-2) +"*")    