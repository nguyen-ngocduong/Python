class MonHoc:
    def __init__(self, id = 1, name = "", so_tc = 1):
        self.__id = id
        self.__name = name
        self.__so_tc = so_tc
    def nhap(self):
        self.__id = int(input("Nhap id mon hoc: "))
        self.__name = input("Nhap ten mon hoc: ")
        self.__so_tc = int(input("Nhap so tin chi: "))
    def show(self):
        print(f"Ma mon: {self.__id} - Ten hoc phan: {self.__name} - So tin: {self.__so_tc} tc")
    def get_so_tc(self):
        return self.__so_tc
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
class HocKy:
    def __init__(self, ma_hoc_ky = 1, so_mon_hoc = 1, danh_sach_mon_hoc = None):
        self.__ma_hoc_ky = ma_hoc_ky
        self.__so_mon_hoc = so_mon_hoc
        self.__danh_sach_mon_hoc = danh_sach_mon_hoc if danh_sach_mon_hoc is not None else []
    def nhap(self):
        self.__ma_hoc_ky = int(input("Nhap ma hoc ky: "))
        self.__so_mon_hoc = int(input("Nhap so mon hoc: "))
        for _ in range(self.__so_mon_hoc):
            mon_hoc = MonHoc()
            mon_hoc.nhap()
            self.__danh_sach_mon_hoc.append(mon_hoc)
    def show(self):
        print(f"Hoc ky {self.__ma_hoc_ky} - so mon: {self.__so_mon_hoc} mon")
        for mon_hoc in self.__danh_sach_mon_hoc:
            mon_hoc.show()
    def get_danh_sach_mon_hoc(self):
        return self.__danh_sach_mon_hoc
    def get_ma_hoc_ky(self):
        return self.__ma_hoc_ky
    def get_ten_hoc_ky(self):
        return self.__so_mon_hoc
    def get_tong_so_tc(self):
        tong_so_tc = 0
        for mon_hoc in self.__danh_sach_mon_hoc:
            tong_so_tc += mon_hoc.get_so_tc()
        return tong_so_tc