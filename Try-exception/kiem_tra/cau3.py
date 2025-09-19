class ThoiGian:
    def __init__(self, gio = "", phut = "",giay = ""):
        self.__gio = gio
        self.__phut = phut
        self.__giay = giay
    def nhap(self):
        self.__gio = (input("Nhap gio: "))
        self.__phut = (input("Nhap phut: "))
        self.__giay = (input("Nhap giay: "))
    def show(self):
        print(f"{self.__gio}:{self.__phut}:{self.__giay}")
    def get_gio(self):
        return self.__gio    
    def get_giay(self):
        return self.__giay
    def get_phut(self):
        return self.__phut
    def so_sanh(self, gio_khac):
        h1, m1, s1 = int(self.__gio), int(self.__phut), int(self.__giay)
        h2, m2, s2 = int(gio_khac.get_gio()), int(gio_khac.get_phut()), int(gio_khac.get_giay())
        if (h1,m1,s1) < (h2,m2,s2):
            return -1
        elif (h1, m1, s1) > (h2,m2,s2):
            return 1
        else:
            return 0
    def khoang_cach_tg(self, gio_khac):
        h1, m1, s1 = int(self.__gio), int(self.__phut), int(self.__giay)
        h2, m2, s2 = int(gio_khac.get_gio()), int(gio_khac.get_phut()), int(gio_khac.get_giay())
        t1 = h1 * 3600 + m1 * 60 + s1
        t2 = h2 * 3600 + m2 * 60 + s2
        khoang_cach = abs(t1-t2)
        gio = khoang_cach // 3600
        phut = (khoang_cach % 3600) // 60
        giay = khoang_cach % 60
        return ThoiGian(gio, phut, giay)
    def tong_thoi_gian(self, gio_2,gio_3):
        t1 = int(self.__gio) * 3600 + int(self.__phut) * 60 + int(self.__giay)
        t2 = int(gio_2.get_gio()) * 3600 + int(gio_2.get_phut()) * 60 + int(gio_2.get_giay())
        t3 = int(gio_3.get_gio()) * 3600 + int(gio_3.get_phut()) * 60 + int(gio_3.get_giay())
        tong = t1 + t2 + t3
        #Chuan hoa:
        tong = tong % (86400) #Tinh ngay
        gio = tong // 3600
        phut = (tong % 3600) // 60
        giay = tong % 60
        return ThoiGian(gio, phut, giay)
    
if __name__ == "__main__":
    gio_1 = ThoiGian()
    gio_1.nhap()
    gio_2 = ThoiGian()
    gio_2.nhap()
    gio_1.show()
    gio_2.show()
    #so sanh
    if gio_1.so_sanh(gio_2) == 1:
        print("Gio 1 lon hon")
    elif gio_1.so_sanh(gio_2) == 0:
        print("Bang nhau")
    else:
        print("Gio 2 lon hon")
    print("Khoang cach giua 2 gio la: ")
    khoang_cach = gio_1.khoang_cach_tg(gio_2)
    khoang_cach.show()
    gio_3 = ThoiGian()
    gio_3.nhap()
    gio_3.show()
    tong_thoi_gian = gio_1.tong_thoi_gian(gio_2, gio_3)
    tong_thoi_gian.show()