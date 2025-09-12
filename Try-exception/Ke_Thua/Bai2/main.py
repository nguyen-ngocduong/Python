from class_file import *
from def_file import *

n = int(input("Nhap so luong nhan vien: "))
ds_nv = []
for _ in range(n):
    nhan_vien = NhanVien()
    nhan_vien.nhap()
    ds_nv.append(nhan_vien)
sap_xep_snct = ds_nv.copy()
sap_xep_snct.sort(key = sap_xep_theo_snct, reverse = True)
print("Nhan vien co so nam cong tac nhieu nhat la: ")
sap_xep_snct[0].show()
luong_cb = float(input("Nhap luong co ban: "))
bonus = float(input("Nhap tien phu cap co ban: "))
sap_xep_tien_luong = ds_nv.copy()
sap_xep_tien_luong.sort(key = lambda nv: sap_xep_theo_tien_luong(nv, luong_cb, bonus), reverse = True)
print("Nhan vien co tien luong cao nhat la: ")
sap_xep_tien_luong[0].show()