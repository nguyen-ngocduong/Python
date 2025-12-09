class Person:
    def __init__(self, ho_ten = "", tuoi = 1):
        self.__ho_ten = ho_ten
        self.__tuoi = tuoi
    def nhap(self):
        self.__ho_ten = input("Nhap ho ten: ")
        self.__tuoi = int(input("Nhap tuoi: "))
    def show(self):
        print(f"{self.__ho_ten} - {self.__tuoi} tuoi")
class NhanVien(Person):
    def __init__(self, ho_ten = "", tuoi = 1, snct = 1, hs_luong = 1.0):
        super().__init__(ho_ten, tuoi)
        self.__snct = snct
        self.__hs_luong = hs_luong
    def nhap(self):
        super().nhap()
        self.__snct = int(input("Nhap so nam cong tac: "))
        self.__hs_luong = float(input("Nhap he so luong: "))
    def show(self):
        super().show()
        print(f"{self.__snct} nam cong tac - he so luong: {self.__hs_luong}")
    def get_tien_luong(self, luong_cb, bonus):
        phu_cap = bonus * self.__snct
        res = luong_cb * self.__hs_luong + phu_cap
        return res
    def get_snct(self):
        return self.__snct