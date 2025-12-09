from class_file import *
from def_file import *

n = int(input("Nhap so luong hoc ky: "))
danh_sach_hoc_ky = []
for _ in range(n):
    hoc_ky = HocKy()
    hoc_ky.nhap()
    danh_sach_hoc_ky.append(hoc_ky)
    # tong_so_tc = tinh_tong_so_tc(danh_sach_hoc_ky)
    # print(f"Tong so tin chi la: {tong_so_tc}")
    for hoc_ky in danh_sach_hoc_ky:
        print(hoc_ky.get_tong_so_tc())
    hoc_ky_nhieu_tc_nhat = tim_hoc_ky_nhieu_tc(danh_sach_hoc_ky)
    print("Hoc ky co nhieu tin chi nhat la: ")
    hoc_ky_nhieu_tc_nhat.show()