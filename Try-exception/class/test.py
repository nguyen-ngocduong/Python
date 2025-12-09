# # Nhap vao 2 sv xem diem sv nao lon hon
# class SinhVien:
#     def __init__(self):
#         self.ten = "A"
#         self.diem = 3.0
#         self.ma = 1
#     def nhap(self):
#         self.ten = input("Nhap ten: ")
#         self.diem = float(input("Nhap diem: "))
#         self.ma = int(input("Nhap ma: "))
#     def show(self):
#         print(f"{self.ma} - {self.ten} - {self.diem}")

# sv1 = SinhVien()
# sv2 = SinhVien()
# sv1.nhap()
# sv2.nhap()
# if sv1.diem > sv2.diem:
#     print(f"Sinh vien {sv1.ten} co diem lon hon")
#     sv1.show()
# else:
#     print(f"Sinh vien {sv2.ten} co diem lon hon")
#     sv2.show()
class phanso:
    def __init__(self):
        self.tu = 1
        self.mau = 1
    def nhap(self):
        self.tu = int(input("Nhap tu so: "))
        self.mau = int(input("Nhap mau so: "))
    def show(self):
        print(f"{self.tu}/{self.mau}")
    def cong(self, phan_so_khac): # da co 1 phan so la self
        tu_moi = self.tu * phan_so_khac.mau + self.mau * phan_so_khac.tu
        mau_moi = self.mau * phan_so_khac.mau
        if mau_moi == 0:
            return "Loi chia 0"
        else: return (f"{tu_moi}/{mau_moi}")
    def tru(self, phan_so_khac):
        tu_moi = self.tu * phan_so_khac.mau - self.mau * phan_so_khac.tu
        mau_moi = self.mau * phan_so_khac.mau
        if mau_moi == 0:
            return "Loi chia 0"
        else:
            return (f"{tu_moi}/{mau_moi}")
    def nhan(self, phan_so_khac):
        tu_moi = self.tu * phan_so_khac.tu
        mau_moi = self.mau * phan_so_khac.mau
        if mau_moi == 0:
            return "Loi chia 0"
        else: return (f"{tu_moi}/{mau_moi}")
    def chia(self, phan_so_khac):
        tu_moi = self.tu * phan_so_khac.mau
        mau_moi = self.mau * phan_so_khac.tu
        if mau_moi == 0:
            return "Loi chia 0"
        else: return (f"{tu_moi}/{mau_moi}")
    def sosanh(self, phan_so_khac):
        if self.tu / self.mau > phan_so_khac.tu / phan_so_khac.mau:
            return f"{self.tu}/{self.mau} lon hon {phan_so_khac.tu}/{phan_so_khac.mau}"
        elif self.tu / self.mau < phan_so_khac.tu / phan_so_khac.mau:
            return f"{self.tu}/{self.mau} nho hon {phan_so_khac.tu}/{phan_so_khac.mau}"
        else: return f"{self.tu}/{self.mau} bang {phan_so_khac.tu}/{phan_so_khac.mau}"
    def nghichdao(self):
        return f"{self.mau}/{self.tu}"
    #Kiem tra xem phan so co lon hon 1 khong
    def lon_hon_1(self):
        if self.tu / self.mau > 1:
            return True
        else:
            return False
phan_so_1 = phanso()
phan_so_1.nhap()
phan_so_1.show()
phan_so_2 = phanso()
phan_so_2.nhap()
phan_so_2.show()
print(phan_so_1.sosanh(phan_so_2))
print(f"Phep cong: {phan_so_1.cong(phan_so_2)}\nPhep tru: {phan_so_1.tru(phan_so_2)}\nPhep nhan: {phan_so_1.nhan(phan_so_2)}\nPhep chia: {phan_so_1.chia(phan_so_2)}")