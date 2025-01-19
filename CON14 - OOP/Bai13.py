#Nhân viên 1
class NhanVien:
    def __init__(self, ma, name, sex, birth, address,ma_thue, sign):
        self.ma = format(ma, '05d')
        self.name = name
        self.sex = sex
        self.birth = birth
        self.address = address
        self.ma_thue = ma_thue
        self.sign = sign
    def chuanhoaten(self):
        tmp = self.name.split()
        res = ' '.join(tmp)
        self.name = res.title()
    def chuanhoabirth(self):
        if self.birth[1] == '/':
            self.birth = '0' + self.birth
        if self.birth[4] == '/':
            self.birth = self.birth[0:3] + '0' + self.birth[3:]
    def chuanhoasign(self):
        if self.sign[1] == '/':
            self.sign = '0' + self.sign
        if self.sign[4] == '/':
            self.sign = self.sign[0:3] + '0' + self.sign[3:]
    def __str__(self):
        # Trả về chuỗi thông tin nhân viên
        return f"{self.ma} {self.name} {self.sex} {self.birth} {self.address} {self.ma_thue} {self.sign}"

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        name = input()
        sex = input()
        tuoi = input()
        address = input()
        mathue = input()
        sign = input()
        nv = NhanVien(i+1, name, sex, tuoi, address, mathue, sign)
        nv.chuanhoabirth()
        nv.chuanhoasign()
        nv.chuanhoaten()
        print(nv)