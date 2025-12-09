class Sach:
    def __init__(self, ma = "", ten = "", tac_gia = "", the_loai = "", gia = 1):
        self.__ma = ma
        self.__ten = ten
        self.__tac_gia = tac_gia
        self.__the_loai = the_loai
        self.__gia = gia
    def nhap(self):
        self.__ma = input("Nhap ma sach: ")
        self.__ten = input("Nhap ten sach: ")
        self.__tac_gia = input("Nhap ten tac gia: ")
        self.__the_loai = input("Nhap the loai: ")
        self.__gia = int(input("Nhap gia sach: "))
    def show(self):
        print(f"{self.__ma} - {self.__ten} - {self.__tac_gia} - {self.__the_loai} - {self.__gia}")
    def get_gia(self):
        return self.__gia
    def get_the_loai(self):
        return self.__the_loai
    def get_tac_gia(self):
        return self.__tac_gia

class ThuVien:
    def __init__(self):
        self.danh_sach = []
    #Nhập vào danh sách n quyển sách.
    def nhap(self):
        n = int(input("Nhap so sach: "))
        for _ in range(n):
            sach = Sach()
            sach.nhap()
            self.danh_sach.append(sach)
    # In ra danh sách các quyển sách thuộc thể loại "Khoa học".
    def in_danh_sach_the_loai(self, the_loai):
        check = False
        for sach in self.danh_sach:
            if sach.get_the_loai() == the_loai:
                check = True
                sach.show()
        if check == False:
            print(f"Khong co sach thuoc the loai {the_loai}")
    # Tính tổng giá tiền của tất cả sách có giá < 100.000
    def tong_gia_duoi(self, nguong_tien):
        tong = 0
        for sach in self.danh_sach:
            if sach.get_gia() < nguong_tien:
                tong += sach.get_gia()
        return tong
    # Nhập vào tên tác giả, đếm và in ra số lượng sách của tác giả đó trong thư viện.
    def so_sach_thuoc_tac_gia(self, ten_tac_gia):
        lst_tm = []
        for sach in self.danh_sach:
            if sach.get_tac_gia() == ten_tac_gia:
                lst_tm.append(sach)
        return lst_tm, len(lst_tm)
    # Tìm và in ra quyển sách có giá cao nhất
    def tim_sach_gia_cao(self):
        gia_cao_nhat = max(self.danh_sach, key= lambda sach: sach.get_gia())
        gia_cao_nhat.show()

if __name__ == "__main__":
    thu_vien = ThuVien()
    thu_vien.nhap()
    the_loai = input("Nhap the loai can tim: ")
    thu_vien.in_danh_sach_the_loai(the_loai)
    nguong_tien = int(input("Nhap gia tien dieu kien: "))
    print(thu_vien.tong_gia_duoi(nguong_tien))
    ten_tac_gia = input("Nhap ten tac gia can tim: ")
    lst, dem = thu_vien.so_sach_thuoc_tac_gia(ten_tac_gia)
    print(f"So sach thuoc {ten_tac_gia} la: {dem} sach")
    for sach in lst:
        sach.show()
    print("Sach co gia lon nhat la: ")
    thu_vien.tim_sach_gia_cao()