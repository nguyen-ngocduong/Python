from class_file import *
from def_file import *

n = int(input("Nhap vao so luong sinh vien: "))
lstSV = []
for _ in range(n):
    sinh_vien = DangKyHocPhan()
    sinh_vien.nhap()
    lstSV.append(sinh_vien)
for sv in lstSV:
    sv.show()
    danh_sach_mon_hoc = sv.get_danh_sach_mon()
    tong_tin_chi = dem_so_tin_chi(danh_sach_mon_hoc)
    print(tong_tin_chi)
ten_mon_hoc = input("Nhap ten mon hoc can tim: ")
new_lst_sv = info_sv_dang_ky_mon(lstSV, ten_mon_hoc)
for sinh_vien in new_lst_sv:
    sinh_vien.show()