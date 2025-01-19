#Sắp xếp sinh viên theo lớp
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
        a.append(sinhvien)
    a.sort(key = lambda x : (x.get_lop(), x.get_ma()))
    for x in a:
        print(x)