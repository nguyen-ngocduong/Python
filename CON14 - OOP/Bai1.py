#Lớp phân số
from math import *
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def toi_gian(self):
        tmp = gcd(self.tu, self.mau)
        self.tu //= tmp
        self.mau //= tmp
    def __str__(self):
        return f'{self.tu}/{self.mau}'
    
if __name__ == '__main__':
    tu, mau = map(int, input().split())
    phanso = PhanSo(tu, mau)
    phanso.toi_gian()
    print(phanso)