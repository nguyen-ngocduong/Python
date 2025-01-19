#Giáo viên chủ nhiệm
class Person:
    def __init__(self, ma, name, tuoi,dia_chi):
        self.ma = ma
        self.name = name
        self.tuoi = tuoi
        self.dia_chi = dia_chi
    def chuanhoaten(self):
        tmp = self.name.split()
        res = ' '.join(tmp)
        self.name = res.title()
    def chuanhoabirth(self):
        if self.tuoi[1] == '/':
            self.tuoi = '0' + self.tuoi
        if self.tuoi[4] == '/':
            self.tuoi = self.tuoi[0:3] + '0' + self.tuoi[3:]
    def get_ma(self):
        return self.ma
    def __str__(self):
        return f'{self.ma} {self.name} {self.tuoi} {self.dia_chi}'
class Student(Person) :
    def __init__(self, ma, name, tuoi, dia_chi,lop,gpa):
        super().__init__(ma, name, tuoi, dia_chi)
        self.gpa = gpa
        self.lop = lop
    def __str__(self):
        return f'{Person.__str__(self)} {self.lop} {self.gpa:.2f}'
    def get_lop(self):
        return self.lop
class GiangVien(Person):
    def __init__(self, ma, name, tuoi, dia_chi,khoa,luong,lop):
        super().__init__(ma, name, tuoi, dia_chi)
        self.khoa = khoa
        self.luong = luong
        self.lop = lop
    def __str__(self):
        return f'{Person.__str__(self)} {self.khoa} {self.luong} {self.lop}'
    def get_luong(self):
        return self.luong
    def get_lop(self):
        return self.lop
if __name__ == '__main__':
    n = int(input())
    sv,gv = [],[]
    for _ in range(n):
        ma = input()
        if ma[:2] == 'GV':
            t = GiangVien(ma, input(), input(), input(), input(), int(input()), input())
            t.chuanhoabirth()
            t.chuanhoaten()
            gv.append(t)
        else:
            s = Student(ma, input(), input(), input(), input(), float(input()))
            s.chuanhoabirth()
            s.chuanhoaten()
            sv.append(s)
    lop = input()
    print('Danh sach giang vien thuoc lop ' + lop + ' :')
    for x in gv:
        if x.get_lop() == lop:
            print(x)
    print('Danh sach sinh vien thuoc lop ' + lop + ' :')
    for x in sv:
        if x.get_lop() == lop:
            print(x)