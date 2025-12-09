from math import *
class Point:
    def __init__(self, hoanh_do = 1.0, tung_do = 1.0):
        self.__hoanh_do = hoanh_do 
        self.__tung_do = tung_do
    def nhap(self):
        self.__hoanh_do = float(input("Nhap hoanh do: "))
        self.__tung_do = float(input("Nhap tung do: "))
    def show(self):
        print(f"Toa do: ({self.__hoanh_do}, {self.__tung_do})")
    def get_hoanh_do(self):
        return self.__hoanh_do
    def get_tung_do(self):
        return self.__tung_do
    def get_distance(self, diem_khac):
        return sqrt((self.__hoanh_do - diem_khac.__hoanh_do) ** 2 + (self.__tung_do - diem_khac.__tung_do) ** 2)
class DaGiac:
    def __init__(self, so_canh = 1, diem = None):
        self.__so_canh = so_canh 
        self.__diem = diem if diem is not None else []
    def nhap(self):
        self.__so_canh = int(input("Nhap so canh cua da giac: "))
        if self.__so_canh < 3:
            print("Khong co da giac nao thoa man")
            self.__diem = []
        else:
            for _ in range(self.__so_canh):
                point = Point()
                point.nhap()
                self.__diem.append(point)
    def show(self):
        print(f"So canh: {self.__so_canh}")
        print("So diem: ")
        for i in range(self.__diem):
            print("Toa do diem {i} la: ")
            self.__diem[i].show()
    def get_so_canh(self):
        return self.__so_canh
    def get_so_diem(self):
        return self.__diem
    def get_chu_vi(self):
        p = 0
        for i in range(self.__so_canh):
            j = (i + 1) % self.__so_canh
            p += self.__diem[i].get_distance(self.__diem[j])
        return p
