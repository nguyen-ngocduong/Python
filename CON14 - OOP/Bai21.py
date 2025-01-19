#Kế thừa kowps Person
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
    def __init__(self,ma, name, birth, address, lop, gpa):
        Person.__init__(self,name, birth, address)
        self.ma = format(ma, '04d')
        self.lop = lop
        self.gpa = gpa
    def __str__(self):
        return f'{self.ma} {Person.show(self)} {self.lop} {self.gpa:.2f}'
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        ten = input()
        ns = input()
        lop = input()
        diem = float(input())
        pos = 0
        for j in range(len(ns)):
            if ns[j].isalpha():
                pos = j
                break
        diachi = ns[pos:]
        ns = ns[:pos]
        s = Student(i+1, ten, ns, diachi, lop, diem)
        s.chuanhoabirth()
        s.chuanhoaten()
        print(s)