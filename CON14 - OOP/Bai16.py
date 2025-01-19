#Bảng điểm
from functools import cmp_to_key
class HocSinh:
    def __init__(self,ma, name, diem):
        self.ma = 'HS' + format(ma, '02d')
        self.name = name
        self.diem = diem
    
    def get_tb(self):
        tong = sum(self.diem)
        return tong / len(self.diem)
    def phan_loai(self):
        res = ''
        if self.get_tb() >= 9:
            res = 'Xuat Sac'
        elif self.get_tb() <9 and self.get_tb() >= 8:
            res = 'Gioi'
        elif self.get_tb() < 8 and self.get_tb() >= 7:
            res = 'Kha'
        elif self.get_tb() >= 5:
            res = 'TB'
        else:
            res = 'Yeu'
        return res
    def __str__(self):
        return f'{self.ma} {self.name} {self.get_tb():.1f} {self.phan_loai()}'
    def get_ma(self):
        return self.ma
def cmp(a,b):
    tb1, tb2 = a.get_tb(), b.get_tb()
    if tb1 != tb2:
        if tb1 > tb2 :
            return -1
        else:
            return 1
    else:
        ma1, ma2 = a.get_ma(), b.get_ma()
        if ma1 < ma2:
            return -1
        else: return 1
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        ten = input()
        diem = list(map(float, input().split()))
        hs = HocSinh(i+1, ten, diem)
        a.append(hs)
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        print(x)