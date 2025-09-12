class LapTop: 
    def __init__(self, id = 1, name = "", category = "", price = 1):
        self.__id = id
        self.__name = name
        self.__category = category
        self.__price = price
    def nhap(self):
        self.__id = int(input("Nhap id laptop: "))
        self.__name = input("Nhap ten laptop: ")
        self.__category = input("Nhap loai: ")
        self.__price = int(input("Nhap gia laptop: "))
    def show(self):
        print(f"{self.__id} - {self.__name} - {self.__category} - {self.__price}")
    def get_category(self):
        return self.__category
    def get_gia(self):
        return self.__price
    def get_ten(self):
        return self.__name
    def get_id(self):
        return self.__id
def thong_ke(categories):
    return categories
def loai_nhieu_nhat(categories):
    output = []
    for loai_may_tinh in categories:
        output.append(categories[loai_may_tinh])
    max_ele = max(output)
    res = []
    for loai, so_luong in categories.items():
        if so_luong == max_ele:
            res.append(loai)
    return res
def dem_loai(lstlaptop, loai):
    count = 0
    for laptop in lstlaptop:
        if laptop.get_category() == loai:
            count += 1
    return count
def laptop_ab(lstlaptop,a,b):
    laptop_thoa_man = []
    for laptop in lstlaptop:
        if laptop.get_gia() >= a and laptop.get_gia() <= b:
            laptop_thoa_man.append(laptop)
    return laptop_thoa_man
def sap_xep_theo_gia(laptop):
    return laptop.get_gia()
n = int(input("Nhap so luong laptop: "))
lstlaptop = []
for _ in range(n):
    laptop = LapTop()
    laptop.nhap()
    lstlaptop.append(laptop)
for laptop in lstlaptop:
    laptop.show()
categories = {"A" : 0, "B" : 0, "C" : 0}
for laptop in lstlaptop:
    loai_may_tinh = laptop.get_category()
    if loai_may_tinh in categories:
        categories[loai_may_tinh] += 1
print(thong_ke(categories))
print(dem_loai(lstlaptop, "A"))
print(dem_loai(lstlaptop, "B"))
print(dem_loai(lstlaptop, "C"))
print(loai_nhieu_nhat(categories))
a,b = map(int, input("Nhap gia [a,b]: ").split())
print("Danh sach laptop co gia trong khoang [a,b]: ")
lst = laptop_ab(lstlaptop, a, b)
for laptop in lst:
    laptop.show()
lstlaptop.sort(key = sap_xep_theo_gia, reverse = True) #key để tùy chỉnh tiêu chí sắp xếp. 
print("Danh sach giam dan: ")
for laptop in lstlaptop:
    laptop.show()