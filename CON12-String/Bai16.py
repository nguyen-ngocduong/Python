#Chuẩn hóa tên 1
# Tần suất các từ xuất hiện trong xâu
if __name__ == '__main__':
    s = input()
    t = input()
    a = s.split()
    print(' '.join(a).title())
    if t[1] == '/':
        t = '0' + t
    if t[4] == '/' :
        t = t[0:3] + '0' + t[3:]
    print(t)