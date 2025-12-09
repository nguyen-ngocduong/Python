class Xe:
    def __init__(self, bien_so = "", weight = 1.0):
        self.__bien_so = bien_so
        self.__weight = weight
    def nhap(self):
        self.__bien_so = input("Nhap bien so: ")
        self.__weight = float(input("Nhap trong tai: "))
    def show(self):
        print(f"Bien so: {self.__bien_so}, Trong tai: {self.__weight} tan")
    def get_weight(self):
        return self.__weight
class XeCon(Xe):
    def __init__(self, bien_so="", weight=1.0, so_cho = 1):
        super().__init__(bien_so, weight)
        self.__so_cho = so_cho
    def nhap(self):
        super().nhap()
        self.__so_cho = int(input("Nhap so cho ngoi: "))
    def show(self):
        super().show()
        print(f"So cho ngoi: {self.__so_cho}")
    def get_so_cho(self):
        return self.__so_cho