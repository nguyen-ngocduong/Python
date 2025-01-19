#Tìm kiếm xe
class Vehicle:
    def __init__(self, ma, ten, hang, mau, gia):
        self.ma = ma
        self.ten = ten
        self.hang = hang
        self.mau = mau
        self.gia = gia
    def __str__(self):
        return f'{self.ma} {self.ten} {self.hang} {self.mau}'
    def get_ten(self):
        return self.ten
class Bike(Vehicle):
    def __init__(self, ma, ten, hang, mau,tocdo, gia):
        super().__init__(ma, ten, hang, mau, gia)
        self.tocdo = tocdo
    def __str__(self):
        return f'{Vehicle.__str__(self)} {self.tocdo} {self.gia}'
    def get_ma(self):
        return self.ma
    def get_gia(self):
        return self.gia
class Car(Vehicle):
    def __init__(self, ma, ten, hang, mau,maluc, gia):
        super().__init__(ma, ten, hang, mau, gia)
        self.maluc = maluc
    def __str__(self):
        return f'{Vehicle.__str__(self)} {self.maluc} {self.gia}'
    def get_ma(self):
        return self.ma
    def get_gia(self):
        return self.gia
if __name__ == '__main__':
    n = int(input())
    car,bike = [],[]
    for _ in range(n):
        ma = input()
        if ma[0] == 'X':
            xemay = Bike(ma, input(), input(), input(), int(input()), int(input()))
            bike.append(xemay)
        else:
            oto = Car(ma,input(), input(), input(), int(input()), int(input()))
            car.append(oto)
    q = input()
    print('Danh sach oto: ')
    for x in car:
        if x.get_ten() == q:
            print(x)
    print('Danh sach xe may: ')
    for x in bike:
        if x.get_ten() == q:
            print(x)