#Tạo email và mật khẩu
# namnv@xyz.edu.vn mk 1952004
if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        s = input().lower()
        a = s.split()
        email = a[-2]
        date = a[-1]
        for i in range(len(a)-2):
            email += a[i][0]
        print(email + '@xyz.edu.vn')
        date = date.split('/')
        for x in date:
            print(int(x), end='')
        print()