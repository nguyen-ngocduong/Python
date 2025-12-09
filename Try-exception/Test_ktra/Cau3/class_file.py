class Xe:
    def __init__(self, bien_so = "", mau = ""):
        self.__bien_so = bien_so
        self.__mau = mau
    def nhap(self):
        self.__bien_so = input("Nhap bien so xe: ")
        self.__mau = input("Nhap mau xe: ")
    def show(self):
        print(f"Bien so: {self.__bien_so} - Mau xe: {self.__mau}")
    def get_bien_so(self):
        return self.__bien_so
    def get_mau(self):
        return self.__mau

class XeOto(Xe):
    def __init__(self, bien_so="", mau="", tai_trong = 1.0, so_cho_ngoi = 1):
        super().__init__(bien_so, mau)
        self.__tai_trong = tai_trong
        self.__so_cho_ngoi = so_cho_ngoi
    def nhap(self):
        super().nhap()
        self.__tai_trong = float(input("Nhap trong luong cua xe: "))
        self.__so_cho_ngoi = int(input("Nhap so cho ngoi cua xe: "))
    def show(self):
        super().show()
        print(f"Tai trong: {self.__tai_trong} - So cho: {self.__so_cho_ngoi}")
    def get_tai_trong(self):
        return self.__tai_trong
    def get_so_cho(self):
        return self.__so_cho_ngoi
class XeMay(Xe):
    def __init__(self, bien_so="", mau="", phan_khoi = 1):
        super().__init__(bien_so, mau)
        self.__phan_khoi = phan_khoi
    def nhap(self):
        super().nhap()
        self.__phan_khoi = int(input("Nhap phan khoi cua xe may: "))
    def show(self):
        super().show()
        print(f"Phan khoi: {self.__phan_khoi}")
