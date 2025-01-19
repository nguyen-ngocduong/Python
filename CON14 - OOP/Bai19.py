#Liệt kê sinh viên theo lớp
class SinhVien:
    def __init__(self, ma, name, lop, email):
        self.ma = ma
        self.name = name
        self.lop = lop
        self.email = email
    def get_lop(self):
        return self.lop
    def get_ma(self):
        return self.ma
    def chuanhoaten(self):
        res = self.name.split()
        tmp = ' '.join(res)
        self.name = tmp.title()
    def __str__(self):
        return f'{self.ma} {self.name} {self.lop} {self.email}'
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        ma = input()
        name = input()
        lop = input()
        email = input()
        sinhvien = SinhVien(ma, name, lop, email)
        sinhvien.chuanhoaten()
        a.append(sinhvien)
    q = int(input())
    for _ in range(q):
        lop = input()
        print('DANH SACH SINH VIEN LOP', lop, ':')
        for x in a:
            if x.get_lop() == lop:
                print(x)