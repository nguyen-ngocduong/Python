h = int(input("Nhập chiều cao h: "))
khoang_trang_ngoai = h-1
khoang_trang_trong = 1
for i in range(h) :
    if i == 0 :
        print(" " * khoang_trang_ngoai + "*")
    elif i < h-1 :
        print(" " * khoang_trang_ngoai + "*" + " " * khoang_trang_trong + "*")
        khoang_trang_trong += 2
    else :
        print("*" * (h*2-1))
    khoang_trang_ngoai -=1     