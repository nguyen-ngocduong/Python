from functools import cmp_to_key

class SinhVien:
    def __init__(self, ma, name, sex, birth,address,cccd,out):
        self.ma = 'SV' + format(ma, '03d')
        self.name = name
        self.sex = sex
        self.birth = birth
        self.address = address
        self.cccd = cccd
        self.out = out
    def chuanhoabirth(self):
        if self.birth[1] == '/':
            self.birth = '0' + self.birth
        if self.birth[4] == '/':
            self.birth = self.birth[0:3] + '0' + self.birth[3:]
        if self.out[1] == '/':
            self.out = '0' + self.out
        if self.out[4] == '/':
            self.out = self.out[0:3] + '0' + self.out[3:]
    def chuanhoaten(self):
        tmp = self.name.split()
        res = ' '.join(tmp)
        self.name = res.title()
    def __str__(self):
        return f'{self.ma} {self.name} {self.sex} {self.birth} {self.address} {self.cccd} {self.out}'
    def get_ns(self):
        return self.birth
    
def cmp(a,b):
    ns1 = a.get_ns()
    ns2 = b.get_ns()
    a1 = list(map(int, ns1.split('/')))
    a2 = list(map(int, ns2.split('/')))
    for i in range(-3,0,1):
        if a1[i] != a2[i]:
            return a1[i] - a2[i]
        ma1, ma2 = a.get_ma(), b.get_ma()
        if ma1 < ma2:
            return -1
        else:
            return 1
        
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        sex = input()
        birth = input()
        address = input()
        cccd = input()
        out = input()
        sinhvien = SinhVien(i+1, name, sex, birth, address, cccd, out)
        sinhvien.chuanhoabirth()
        sinhvien.chuanhoaten()
        a.append(sinhvien)
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        print(x)