#Sinh viên 2
class SinhVien:
    def __init__(self, ma, name, lop, birth,gpa):
        self.ma = 'SV' + format(ma, '03d')
        self.name = name
        self.lop = lop
        self.birth = birth
        self.gpa = gpa

    def chuanhoabirth(self):
        if self.birth[1] == '/':
            self.birth = '0' + self.birth
        if self.birth[4] == '/':
            self.birth = self.birth[0:3] + '0' + self.birth[3:]

    def chuanhoaten(self):
        tmp = self.name.split()
        res = ' '.join(tmp)
        self.name = res.title()

    def __str__(self):
        return f'{self.ma} {self.name} {self.lop} {self.birth} {self.gpa:.2f}'
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        name = input()
        lop = input()
        birth = input()
        gpa = float(input())
        sinhvien = SinhVien(i+1, name, lop, birth, gpa)
        sinhvien.chuanhoabirth()
        sinhvien.chuanhoaten()
        print(sinhvien)