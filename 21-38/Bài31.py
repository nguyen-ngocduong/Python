h = int(input("Nhập chiều cao h: "))
khoang_trong = h-1
for i in range (h) :
    if i==0 :
        print(" " * khoang_trong + "*")
    elif i < h-1 :
        khoang_trong -= 1
        print(" " * khoang_trong + "*" * (i+1))
    else :
        print("*" * h)       