#xét tuyển đại học
class SinhVien:
    def __init__(self, name, email, sdt, diem):
        self.name = name
        self.email = email
        self.sdt = sdt
        self.diem = diem
    def get_tong_diem(self):
        return sum(map(float,self.diem.split()))
    def __str__(self):
        return self.name + '\n' + self.email + '\n' + self.sdt + '\n' + str(self.get_tong_diem()) + '\n'
infile = open('logs/diemthi.txt', 'r')
outfile = open('logs/trungtuyen.txt', 'w')
data = []
for line in infile:
    data.append(line)
a = []
for i in range(0,len(data),4):#đọc 4 dòng liên tiếp
    ten = data[i]
    email = data[i+1]
    sdt = data[i+2]
    diem = data[i+3]
    sv = SinhVien(ten, email, sdt, diem)
    a.append(sv)
a.sort(key = lambda x : x.get_tong_diem(), reverse=True)
for sv in a:
    if sv.get_tong_diem() >= 27:
        outfile.write(str(sv))
infile.close()
outfile.close()