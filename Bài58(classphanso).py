from math import gcd

class Phanso:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def toi_gian(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def __str__(self):
        return f'{self.tu} / {self.mau}'

if __name__ == '__main__':
    # Nhập dữ liệu từ người dùng
    tu, mau = map(int, input("Nhập tử và mẫu (cách nhau bởi khoảng trắng): ").split())
    p = Phanso(tu, mau)
    p.toi_gian()
    print(p)
