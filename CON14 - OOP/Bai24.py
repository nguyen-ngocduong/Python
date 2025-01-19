#Truy vấn sinh viên, giáo viên
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
    def get_diachi(self):
        return self.dia_chi
    def __str__(self):
        return f'{self.ma} {self.name} {self.tuoi} {self.dia_chi}'
class Student(Person) :
    def __init__(self, ma, name, tuoi, dia_chi,lop,gpa):
        super().__init__(ma, name, tuoi, dia_chi)
        self.gpa = gpa
        self.lop = lop
    def __str__(self):
        return f'{Person.__str__(self)} {self.lop} {self.gpa:.2f}'
class GiangVien(Person):
    def __init__(self, ma, name, tuoi, dia_chi,khoa,luong):
        super().__init__(ma, name, tuoi, dia_chi)
        self.khoa = khoa
        self.luong = luong
    def __str__(self):
        return f'{Person.__str__(self)} {self.khoa} {self.luong}'
if __name__ == '__main__':
    n = int(input())
    sv,gv = [],[]
    for _ in range(n):
        ma = input()
        if ma[:2] == 'GV':
            t = GiangVien(ma, input(), input(), input(), input(), int(input()))
            t.chuanhoabirth()
            t.chuanhoaten()
            gv.append(t)
        else:
            s = Student(ma, input(), input(), input(), input(), float(input()))
            s.chuanhoabirth()
            s.chuanhoaten()
            sv.append(s)
    dc = input()
    print('Danh sach giang vien co dia chi tai ' + dc + ' la:')
    for x in gv:
        if x.get_diachi() == dc:
            print(x)
    print('Danh sach sinh vien co dia chi tai ' + dc + ' la:')
    for x in sv:
        if x.get_diachi() == dc:
            print(x)