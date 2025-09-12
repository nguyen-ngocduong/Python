class Person:
    def __init__(self, name = "", age = 1):
        self.__name = name
        self.__age = age
    def nhap(self):
        self.__name = input("Nhap ten: ")
        self.__age = int(input("Nhap tuoi: "))
    def show(self):
        print(f"Ten: {self.__name} - Tuoi: {self.__age}")
class QuanLy(Person):
    def __init__(self, name="", age=1, snct = 1, hsl = 1.0):
        super().__init__(name, age)
        self.__snct = snct
        self.__hsl = hsl
    def nhap(self):
        super().nhap()
        self.__snct = int(input("Nhap so nam cong tac: "))
        self.__hsl = float(input("Nhap he so luong: "))
    def show(self):
        super().show()
        print(f"So nam cong tac: {self.__snct} - He so luong: {self.__hsl}")
    def tinh_luong(self, luong_co_ban):
        if self.__snct < 5:
            return luong_co_ban * self.__hsl + 1*self.__snct
        elif 5 <= self.__snct < 15:
            return luong_co_ban * self.__hsl + 2*self.__snct
        else:
            return luong_co_ban * self.__hsl + 3*self.__snct