class NguoiChoi:

    def __init__(self, username, password, ten, vao, ra):
        self.username= username
        self.password = password
        self.ten = ten
        self.vao = vao
        self.ra = ra
        
    def get_gio_choi(self):
        h1, m1 = int(self.vao[0:2]), int(self.vao[3:])
        h2, m2 = int(self.ra[0:2]), int(self.ra[3:])
        time1 = h1*60 + m1
        time2 = h2*60 + m2
        return time2 - time1
    
    def get_username(self):
        return self.username
    
    def __str__(self):
        phut_choi = self.get_gio_choi()
        h = phut_choi // 60
        m = phut_choi % 60
        return f'{self.username} {self.password} {self.ten} {h} gio {m} phut'
    
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        username = input()
        password = input()
        ten = input()
        vao = input()
        ra = input()
        nguoichoi = NguoiChoi(username, password, ten, vao, ra)
        a.append(nguoichoi)
        
    a.sort(key = lambda x : (-x.get_gio_choi(), x.get_username()))
    for x in a:
        print(x)