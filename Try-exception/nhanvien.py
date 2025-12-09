class NhanVien:
    def __init__(self, ma_nv = 1, ten_nv = "", nam_cong_tac = 1, he_so_luong = 1.0):
        self.__ma_nv = ma_nv
        self.__ten_nv = ten_nv
        self.__nam_cong_tac = nam_cong_tac
        self.__he_so_luong = he_so_luong
    def nhap(self):
        self.__ma_nv = int(input("Nhap ma nv: "))
        self.__ten_nv = input("Nhap ten nv: ")
        self.__nam_cong_tac = int(input("Nhap so nam cong tac: "))
        self.__he_so_luong = float(input("Nhap he so luong: "))
    def show(self):
        print(f"{self.__ma_nv} - {self.__ten_nv} - {self.__nam_cong_tac} - {self.__he_so_luong}")
    def get_nam_cong_tac(self):
        return self.__nam_cong_tac
    def get_he_so_luong(self):
        return self.__he_so_luong
    def get_luong(self, luong_co_ban = 1.8):
        return luong_co_ban*self.get_he_so_luong()*self.get_nam_cong_tac()
    def show_luong(self):
        print(f"{self.__ten_nv} - {self.get_luong()}")
    def get_ten(self):
        return self.__ten_nv

n = int(input("Nhap so nhan vien: "))
lstNV = []
for _ in range(n):
    nv = NhanVien()
    nv.nhap()
    lstNV.append(nv)
for nv in lstNV:
    nv.show_luong()
try:
    ten_nhan_vien = input("Nhap ten nhan vien: ")
except Exception as e:
    print(e)
check = False
for nv in lstNV:
    if nv.get_ten() == ten_nhan_vien:
        check = True
        nv.show()
if check == False:
    print(f"Ko co nv {ten_nhan_vien}")