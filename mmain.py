# Nhập ngày, tháng, năm hiện tại
ngay = int(input("Nhập ngày hiện tại: "))
thang = int(input("Nhập tháng hiện tại: "))
nam = int(input("Nhập năm hiện tại: "))

# Kiểm tra xem tháng hiện tại có bao nhiêu ngày
if thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay_trong_thang = 31
elif thang in [4, 6, 9, 11]:
    so_ngay_trong_thang = 30
else:
    # Nếu là tháng 2, kiểm tra năm nhuận
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        so_ngay_trong_thang = 29
    else:
        so_ngay_trong_thang = 28


# Tính toán ngày mai
if ngay < so_ngay_trong_thang:
    ngay_mai = ngay + 1
    thang_mai = thang
    nam_mai = nam
else:
    ngay_mai = 1
    if thang < 12:
        thang_mai = thang + 1
        nam_mai = nam
    else:
        thang_mai = 1
        nam_mai = nam + 1

# In ra ngày mai
print(f"Ngày mai là ngày {ngay_mai} tháng {thang_mai} năm {nam_mai}")
