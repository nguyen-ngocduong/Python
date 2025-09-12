from class_file import *
from def_file import *
print("Nhap so cty phan mem va so cty van tai: ")
n, m = map(int, input().split())
lstctypm = []
lstctyvt = []
for ctypm in range(n):
    print(f"Nhap thong tin cty phan mem thu {ctypm + 1}: ")
    cty = CTYPM()
    cty.nhap()
    lstctypm.append(cty)
for ctyvt in range(m):
    print(f"Nhap thong tin cty van tai thu {ctyvt + 1}: ")
    cty = CTYVT()
    cty.nhap()
    lstctyvt.append(cty)
nam_thanh_lap = int(input("Nhap nam thanh lap can yeu cau: "))
so_ltv = int(input("Nhap so luong thanh vien can yeu cau: "))
so_oto = int(input("Nhap so luong oto can yeu cau: "))
new_lstctypm = ten_cty_pmen_tm_dk(lstctypm, nam_thanh_lap, so_ltv)
new_lstctyvt = ten_cty_vt_tm_dk(lstctyvt, nam_thanh_lap, so_oto)
print(f"Cac cong ty pmem thanh lap sau nam {nam_thanh_lap} va so ltv > {so_ltv} la: ")
for cty in new_lstctypm:
    cty.show()
print(f"Cac cong ty pmem thanh lap truoc nam {nam_thanh_lap} va so oto <= {so_oto} la: ")
for cty in new_lstctyvt:
    cty.show()
