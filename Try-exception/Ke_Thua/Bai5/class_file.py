class Person:
    def __init__(self, name = "", nam_sinh = 1):
        self.__name = name
        self.__nam_sinh = nam_sinh
    def nhap(self):
        self.__name = input("Nhap ten: ")
        self.__nam_sinh = int(input("Nhap nam sinh: "))
    def show(self):
        print(f"Ten: {self.__name}, Nam sinh: {self.__nam_sinh}")
class Student(Person):
    def __init__(self, name="", nam_sinh=1, diem_tb = 0.0):
        super().__init__(name, nam_sinh)
        self.__diem_tb = diem_tb
    def nhap(self):
        super().nhap()
        self.__diem_tb = float(input("Nhap diem trung binh: "))
    def show(self):
        super().show()
        print(f"Diem trung binh: {self.__diem_tb}")
    def get_diem_tb(self):
        return self.__diem_tb
class GiangVien(Person):
    def __init__(self, name = "", nam_sinh = 1, so_gio_day = 0):
        super().__init__(name, nam_sinh)
        self.__so_gio_day = so_gio_day
    def nhap(self):
        super().nhap()
        self.__so_gio_day = int(input("Nhap so gio day: "))
    def show(self):
        super().show()
        print(f"So gio day: {self.__so_gio_day}")
    def get_so_gio_day(self):
        return self.__so_gio_day