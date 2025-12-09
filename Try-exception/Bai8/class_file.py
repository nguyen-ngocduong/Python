class MonHoc:
    def __init__(self, ma_mon = "", ten_mon = "", so_tc = 1):
        self.__ma_mon = ma_mon
        self.__ten_mon = ten_mon
        self.__so_tc = so_tc
    def nhap(self):
        self.__ma_mon = input("Nhap ma mon hoc: ")
        self.__ten_mon = input("Nhap ten mon hoc: ")
        self.__so_tc = int(input("Nhap so tin chi cua mon hoc do: "))
    def show(self):
        print(f"{self.__ma_mon} - {self.__ten_mon} - {self.__so_tc}")
    def get_ma_mon(self):
        return self.__ma_mon
    def get_ten_mon(self):
        return self.__ten_mon
    def get_so_tc(self):
        return self.__so_tc
class DangKyHocPhan:
    def __init__(self, ma_sv = "", ten_sv = "", danh_sach_mon_hoc = None):
        self.__ma_sv = ma_sv
        self.__ten_sv = ten_sv
        self.__danh_sach_mon_hoc = danh_sach_mon_hoc if danh_sach_mon_hoc is not None else []
    def nhap(self):
        self.__ma_sv = input("Nhap ma sinh vien: ")
        self.__ten_sv = input("Nhap ten sinh vien: ")
        n = int(input("Nhap vao so luong mon hoc: "))
        for i in range(n):
            mon_hoc = MonHoc()
            mon_hoc.nhap()
            self.__danh_sach_mon_hoc.append(mon_hoc)
    def show(self):
        print(f"{self.__ma_sv} - {self.__ten_sv}")
        print("Danh sach mon hoc:")
        for mon in self.__danh_sach_mon_hoc:
            mon.show()
    def get_ma_sv(self):
        return self.__ma_sv
    def get_ten_sv(self):
        return self.__ten_sv
    def get_danh_sach_mon(self):
        return self.__danh_sach_mon_hoc