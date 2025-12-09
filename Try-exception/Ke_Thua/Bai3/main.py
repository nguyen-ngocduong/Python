from class_file import *
def sap_xep_theo_tien_luong(quan_ly, luong_co_ban):
    return quan_ly.tinh_luong(luong_co_ban)

n = int(input("Nhap sao luong quan ly: "))
lst_quan_ly = []
for _ in range(n):
    ql = QuanLy()
    ql.nhap()
    lst_quan_ly.append(ql)
luong_co_ban = float(input("Nhap luong co ban: "))
lst_quan_ly.sort(key = lambda quan_ly: sap_xep_theo_tien_luong(quan_ly, luong_co_ban), reverse=True)
print("Quan ly co tien luong cao nhat: ")
lst_quan_ly[0].show()
print(f"Tien luong: {lst_quan_ly[0].tinh_luong(luong_co_ban)}")
print("Quan ly co tien luong thap nhat: ")
lst_quan_ly[-1].show()
print(f"Tien luong: {lst_quan_ly[-1].tinh_luong(luong_co_ban)}")