from math import *
class SoPhuc:
    def __init__(self, thuc=0, ao = 0):
        self.thuc = thuc
        self.ao = ao
    def nhap(self):
        self.thuc = float(input("Nhap phan thuc cua so phuc: "))
        self.ao = float(input("Nhap phan ao cua so phuc: "))
    def show(self):
        print(f"{self.thuc} + {self.ao}i")
    #tinh module
    def cal_module(self):
        module = sqrt(self.thuc ** 2 + self.ao ** 2)
        return module
    #so sanh 2 so phuc
    def so_sanh(self, so_phuc_moi):
        if self.cal_module() > so_phuc_moi.cal_module():
            return 1
        elif self.cal_module() == so_phuc_moi.cal_module():
            return 0
        else:
            return -1
    #Cong 2 so phuc
    def add(self, so_phuc_moi):
        thuc_moi = self.thuc + so_phuc_moi.thuc
        ao_moi = self.ao + so_phuc_moi.ao
        #so_phuc = f"{thuc_moi} + {ao_moi}i"
        return SoPhuc(thuc_moi, ao_moi)

def main():
    so_phuc_1 = SoPhuc()
    so_phuc_2 = SoPhuc()
    print("Nhap so phuc 1: ")
    so_phuc_1.nhap()
    so_phuc_1.show()
    print(f"Module cua so phuc 1: {so_phuc_1.cal_module():.3f}")
    print("Nhap so phuc 2: ")
    so_phuc_2.nhap()
    so_phuc_2.show()
    print(f"Module cua so phuc 2: {so_phuc_2.cal_module()}")
    #So sanh 2 so phuc
    if so_phuc_1.so_sanh(so_phuc_2) == 1:
        print(f"{so_phuc_1.thuc} + {so_phuc_1.ao}i lon hon {so_phuc_2.thuc} + {so_phuc_2.ao}i")
    elif so_phuc_1.so_sanh(so_phuc_2) == 0: 
        print(f"{so_phuc_1.thuc} + {so_phuc_1.ao}i bang {so_phuc_2.thuc} + {so_phuc_2.ao}i")
    else:
        print(f"{so_phuc_1.thuc} + {so_phuc_1.ao}i nho hon {so_phuc_2.thuc} + {so_phuc_2.ao}i")
    #Cong 2 so phuc
    print("Tong 2 so phuc la: ")
    so_phuc_1.add(so_phuc_2).show()