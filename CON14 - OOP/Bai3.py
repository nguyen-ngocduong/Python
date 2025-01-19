#Lớp sinh viên
class SinhVien:
    def __init__(self, name, lop, birth, gpa):
        self.name = name
        self.lop = lop
        self.birth = birth
        self.gpa = gpa
    def chuanhoa(self):
        if self.birth[1] == '/':
            self.birth = '0' + self.birth
        if self.birth[4] == '/':
            self.birth = self.birth[0:3] + '0' + self.birth[3:]
    def __str__(self):
        return f'SV001 {self.name} {self.lop} {self.birth} {self.gpa}'
if __name__ == '__main__':
    ten = input()
    lop = input()
    tuoi = input()
    gpa = float(input())
    sv = SinhVien(ten, lop, tuoi, gpa)
    sv.chuanhoa()
    print(sv)