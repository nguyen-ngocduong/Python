import math
class hcn:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def dien_tich(self) :
        s = self.chieu_dai * self.chieu_rong
        return s
    def chu_vi(self) :
        cv = (self.chieu_dai + self.chieu_rong ) * 2
        return cv
    def do_dai_cheo(self) :
        cheo = math.sqrt(self.chieu_dai**2 + self.chieu_rong**2)
        return cheo
h1 = hcn(10,8)
print(h1.do_dai_cheo(), end = " ")
print(h1.dien_tich(), end = " ")
print(h1.chu_vi(), end = " ")  