#Lớp nhân viên
class NhanVien:
    def __init__(self, name, sex, born, address, mathue, sign):
        self.name = name
        self.sex = sex
        self.born = born
        self.address = address
        self.mathue = mathue
        self.sign = sign
    def chuanhoaborn(self):
        if self.born[1] == '/':
            self.born = '0' + self.born
        if self.born[4] == '/':
            self.born = self.born[0:3] + '0' + self.born[3:]
    def chuanhoasign(self):
        if self.sign[1] == '/':
            self.sign = '0' + self.sign
        if self.sign[4] == '/':
            self.sign = self.sign[0:3] + '0' + self.sign[3:]
    def __str__(self):
        return f'NV001 {self.name} {self.born} {self.address} {self.mathue} {self.sign}'
    
if __name__ == '__main__':
    name = input()
    sex = input()
    tuoi = input()
    address = input()
    mathue = input()
    sign = input()
    nv = NhanVien(name, sex, tuoi, address, mathue, sign)
    nv.chuanhoaborn()
    nv.chuanhoasign()
    print(nv)