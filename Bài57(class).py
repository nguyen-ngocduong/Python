def UCLN(a,b) :
    if a>b :
        i = b
    else :
        i = a
    while a%i != 0 or b%i != 0 :
        i = i-1 #giảm i để tìm số nhỏ hơn
    return i 
class Phanso :
    def __init__(self, Mauso, Tuso) :
        self.Mauso = Mauso
        self.Tuso = Tuso
        self.ktra = True #ktra xem mẫu có hợp lệ không
        if self.Mauso == 0:
            self.ktra = False
    def in_phanso(self) :
        if self.ktra == False :
            print("Lỗi!")
            return 
        print(self.Mauso ,"/",self.Tuso)
    def rutgon(self) :
        if self.ktra == False:
            print("Lỗi!")
            return #Kết thúc lệnh
        x = UCLN(self.Tuso, self.Mauso)
        self.Tuso = self.Tuso // x
        self.Mauso = self.Mauso // x
        print(self.Tuso ,"/", self.Mauso)
phan_so = Phanso(0, 5)
phan_so.in_phanso()
phan_so.rutgon() 