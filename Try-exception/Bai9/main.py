from class_file import *
from def_file import *

n = int(input("Nhap vao so luong da giac: "))
lstDaGiac = []
for _ in range(n):
    dagiac = DaGiac()
    dagiac.nhap()
    lstDaGiac.append(dagiac)
try:
    tong = 0
    for dagiac in lstDaGiac:
        if dagiac.get_so_canh() < 3:
            print("Da giac khong hop le!")
            continue
        chu_vi = dagiac.get_chu_vi()
        tong += chu_vi
        print(f"Chu vi cua da giac {dagiac.get_so_canh()} canh la: {chu_vi}")
    res = tong / n
    print(f"Tong trung binh chu vi cua {n} da giac la: {res}")
except Exception as e:
    print(e)