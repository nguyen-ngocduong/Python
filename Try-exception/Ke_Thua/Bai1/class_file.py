class CTY:
    def __init__(self, ten = "", ntl = 1):
        self.__ten = ten
        self.__ntl = ntl
    def nhap(self):
        self.__ten = input("Nhap ten cong ty: ")
        self.__ntl = int(input("Nhap nam thanh lap: "))
    def show(self):
        print(f"Ten cty: {self.__ten} - Nam thanh lap: {self.__ntl}")
    def get_ntl(self):
        return self.__ntl
class CTYPM(CTY):
    def __init__(self, ten="", ntl=1, sltv = 1):
        super().__init__(ten, ntl)
        self.__sltv = sltv
    def nhap(self):
        super().nhap()
        self.__sltv = int(input("Nhap so luong thanh vien: "))
    def show(self):
        super().show()
        print(f"So luong thanh vien: {self.__sltv}")
    def get_sltv(self):
        return self.__sltv
class CTYVT(CTY):
    def __init__(self, ten = "", ntl = 1, soto = 1):
        super().__init__(ten, ntl)
        self.__soto = soto
    def nhap(self):
        super().nhap()
        self.__oto = int(input("Nhap so luong oto: "))
    def show(self):
        super().show()
        print(f"So luong oto: {self.__soto}")
    def get_soto(self):
        return self.__soto
