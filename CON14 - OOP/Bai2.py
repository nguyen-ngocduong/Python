#Lớp sinh viên
class SinhVien:
    def __init__(self, name, birth, diem1, diem2, diem3):
        self.name = name
        self.birth = birth
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
    def __str__(self):
        tong_diem = self.diem1 + self.diem2 + self.diem3
        return f'{self.name} {self.birth} {tong_diem:.1f}'
if __name__ == '__main__':
    ten = input()
    ns = input()
    m1,m2,m3 = map(float, input().split())
    sv = SinhVien(ten, ns, m1, m2, m3)
    print(sv)