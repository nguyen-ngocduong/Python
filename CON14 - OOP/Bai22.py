#Kế thừa lớp Person và sắp xếp theo tên
class Person:
    def __init__(self, name, birth, address):
        self.name = name
        self.birth = birth
        self.address = address
    def chuanhoaten(self):
        tmp = self.name.split()
        res = ' '.join(tmp)
        self.name = res.title()
    def chuanhoabirth(self):
        if self.birth[1] == '/':
            self.birth = '0' + self.birth
        if self.birth[4] == '/':
            self.birth = self.birth[0:3] + '0' + self.birth[3:]
    def show(self):
        return f'{self.name} {self.birth} {self.address}'
class Student(Person):
    def __init__(self,ma , name, birth, address, lop, gpa):
        Person.__init__(self, name, birth, address)
        self.ma = format(ma, '04d')
        self.lop = lop
        self.gpa = gpa
    def __str__(self):
        return f'{self.ma} {Person.show(self)} {self.lop} {self.gpa:.2f}'
def cmp_ten(student):
    name_parts = student.name.split()
    last_name = name_parts[-1]  # Tên chính
    first_names = ' '.join(name_parts[:-1])  # Họ và tên đệm
    return (last_name, first_names)  # Trả về tuple để sắp xếp
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        ten = input()
        ns = input()
        address = input()
        lop = input()
        diem = float(input())
        sinhvien = Student(i+1, ten, ns, address, lop, diem)
        sinhvien.chuanhoabirth()
        sinhvien.chuanhoaten()
        a.append(sinhvien)
    a.sort(key = cmp_ten)
    for x in a:
        print(x)