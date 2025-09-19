class PhanSo:
    def __init__(self, tu_so = 1, mau_so = 1):
        self.__tu_so = tu_so
        self.__mau_so = mau_so
    def nhap(self):
        self.__tu_so = int(input("Nhap tu so: "))
        self.__mau_so = int(input("Nhap mau so: "))
    def show(self):
        print(f"{self.__tu_so}/{self.__mau_so}")
    def get_tu_so(self):
        return self.__tu_so
    def get_mau_so(self):
        return self.__mau_so
    def so_sanh(self, phan_so_khac):
        if self.__tu_so * phan_so_khac.get_mau_so() > self.__mau_so * phan_so_khac.get_tu_so():
            return 1
        else: return 0
    def cong_phan_so(self, phan_so_khac):
        tu_so_moi = self.__tu_so * phan_so_khac.get_mau_so() + self.__mau_so * phan_so_khac.get_tu_so()
        mau_so_moi = self.__mau_so * phan_so_khac.get_mau_so()
        return PhanSo(tu_so_moi, mau_so_moi)
    def tich_phan_so(self, phan_so_khac):
        tu_so_moi = self.__tu_so * phan_so_khac.get_tu_so()
        mau_so_moi = self.__mau_so * phan_so_khac.get_mau_so()
        return PhanSo(tu_so_moi, mau_so_moi)
    def hieu_phan_so(self, phan_so_khac):
        tu_so_moi = self.__tu_so * phan_so_khac.get_mau_so() - self.__mau_so * phan_so_khac.get_tu_so()
        mau_so_moi = self.__mau_so * phan_so_khac.get_mau_so()
        return PhanSo(tu_so_moi, mau_so_moi)
    def tinh_gia_tri(self, phan_so_1, phan_so_2):
        tich = phan_so_1.tich_phan_so(phan_so_2)
        gia_tri = self.hieu_phan_so(tich)
        return gia_tri

if __name__ == "__main__":
    phan_so_1 = PhanSo()
    phan_so_1.nhap()
    phan_so_2 = PhanSo()
    phan_so_2.nhap()
    phan_so_3 = PhanSo()
    phan_so_3.nhap()
    phan_so_1.show()
    phan_so_2.show()
    phan_so_3.show()
    if phan_so_1.so_sanh(phan_so_2):
        print("Phan so 1 lon hon phan so 2")
    else: print("Phan so 1 nho hon phan so 2")
    #Cong 2 phan so 1 va 2
    tong_phan_so = phan_so_1.cong_phan_so(phan_so_2)
    tong_phan_so.show()
    #Tinh gia tri bieu thuc:
    gia_tri = phan_so_1.tinh_gia_tri(phan_so_2, phan_so_3)
    gia_tri.show()