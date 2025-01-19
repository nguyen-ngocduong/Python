#Thu nhập lương nhân viên
class GiaoVien:
    def __init__(self, ma, name, luong):
        self.name = name
        self.ma = ma
        self.luong = luong
    def get_he_so(self):
        return int(self.ma[2:])
    def luong_thang(self):
        heso = self.get_he_so()
        luongthang = heso*self.luong
        congviec = self.ma[0:2]
        if congviec == 'HT':
            return luongthang + 2000000
        elif congviec == 'HP':
            return luongthang + 1000000
        else:
            return luongthang + 500000
    def __str__(self):
        return f'{self.ma} {self.name} {self.get_he_so()} {self.luong_thang()}'
    
if __name__ == '__main__':
    ma = input()
    name = input()
    luong = int(input())
    gv = GiaoVien(ma, name, luong)
    print(gv)