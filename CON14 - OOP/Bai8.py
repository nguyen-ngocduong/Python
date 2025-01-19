#Tuyển sinh
class ThiSinh:
    def __init__(self, ma, ten, toan, ly, hoa):
        self.ma = ma
        self.ten = ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    def get_diem_uu_tien(self):
        diem_uu_tien = 0
        if self.ma[0:3] == 'KV1':
            diem_uu_tien += 0.5
        elif self.ma[0:3] == 'KV2':
            diem_uu_tien += 1.0
        else:
            diem_uu_tien += 2.5
        return diem_uu_tien
    def tong_3_mon(self):
        return self.toan + self.ly + self.hoa
    def tong_diem(self):
        return self.tong_3_mon() + self.get_diem_uu_tien()
    def check(self):
        return "TRUNG TUYEN" if self.tong_diem() >= 24 else "TRUOT"
    def __str__(self):
        return f'{self.ma} {self.ten} {self.get_diem_uu_tien()} {self.tong_diem()} {self.check()}'
if __name__ == '__main__':
    ma = input()
    ten = input()
    toan = float(input())
    ly = float(input())
    hoa = float(input())
    thisinh = ThiSinh(ma, ten, toan, ly, hoa)
    print(thisinh) 