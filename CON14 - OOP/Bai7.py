#tính lương nhân viên
class NhanVien:
    def __init__(self, name, luong, ngay_cong, chuc_vu):
        self.name = name
        self.luong = luong
        self.ngay_cong = ngay_cong
        self.chuc_vu = chuc_vu
    def get_luong_thang(self):
        return self.ngay_cong * self.luong 
    def get_thuong(self):
        thuong = 0
        if self.ngay_cong >= 25:
            thuong += int(0.2 * float(self.get_luong_thang()))
        elif  self.ngay_cong < 25 and self.ngay_cong >= 22:
            thuong += int(0.1 * float(self.get_luong_thang()))
        else: thuong = 0
        return thuong
    def get_phu_cap(self):
        thuong = 0
        congviec = self.chuc_vu
        if congviec == 'GD':
            thuong += 250000
        elif congviec == 'PGD':
            thuong += 200000
        elif congviec == 'TP':
            thuong += 180000
        else:
            thuong += 150000
        return thuong
    def tong_luong(self):
        return self.get_phu_cap() + self.get_luong_thang() + self.get_thuong()
    def __str__(self):
        return f'NV001 {self.name} {self.get_luong_thang()} {self.get_thuong()} {self.get_phu_cap()} {self.tong_luong()}'
    
if __name__ == '__main__':
    name, luong, ngay_cong, chuc_vu = input(), int(input()), int(input()), input()
    nhanvien = NhanVien(name, luong, ngay_cong, chuc_vu)
    print(nhanvien)
