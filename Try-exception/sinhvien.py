class SinhVien:
    def __init__(self, ma = 1, ten = "", cccd = ""):
        self.ma = ma # => private: self.__ma = ma
        self.ten = ten
        self.__cccd = cccd
    def nhap(self):
        self.ma = input("Nhap ma sinh vien: ")
        self.ten = input("Nhap ten sinh vien: ")
        self.__cccd = input("Nhap cccd sinh vien: ")
    def show(self):
        print(f"{self.ma} - {self.ten}")
    def get_cccd(self):
        return self.__cccd
    def set_cccd(self, cccd_moi):
        self.__cccd = cccd_moi
        
sv = SinhVien()
sv.nhap()
sv.show()
print(sv.get_cccd())