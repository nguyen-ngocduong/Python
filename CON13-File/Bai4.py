#Cấp email sinh viên
def out_email(s):
    a = s.lower().split()
    email = a[-1]
    for i in range(0,len(a)-1):
        email += a[i][0]
    email += '@ptit.edu.vn'
    return email
def matkhau(s):
    a = s.split('/')
    res = ''
    for x in a:
        res += str(int(x))
    return res
infile = open('logs/sinhvien.txt', 'r')
outfile = open('logs/email.txt', 'w')
data = []
for line in infile:
    data.append(line)
for i in range(0, len(data)):
    if i%2 == 0:
        outfile.write(out_email(data[i]) + '\n')
    else:
        outfile.write(matkhau(data[i]) + '\n')
infile.close()
outfile.close()
# if __name__ == '__main__':
#     s1 = input()
#     s2 = input()
#     print(out_email(s1))
#     print(matkhau(s2))