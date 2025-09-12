from class_file import *

n = int(input("Nhap so luong giang vien va sinh vien: "))
ds_gv = []
ds_sv = []
for _ in range(n):
    loai = input("Nhap loai (1 - giang vien, 2 - sinh vien): ")
    if loai == '1':
        gv = GiangVien()
        gv.nhap()
        ds_gv.append(gv)
    elif loai == '2':
        sv = Student()
        sv.nhap()
        ds_sv.append(sv)
    else:
        print("Loai khong hop le!")
x = int(input("Nhap so gio day: "))
print(f"\nDanh sach giang vien co gio day > {x}: ")
for gv in ds_gv:
    if gv.get_so_gio_day() > x:
        gv.show()
y = float(input("Nhap diem trung binh: "))
print(f"\nDanh sach sinh vien co diem trung binh > {y}: ")
for sv in ds_sv:
    if sv.get_diem_tb() > y:
        sv.show()