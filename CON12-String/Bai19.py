#Tạo email và mật khẩu 2
# Tần suất các từ xuất hiện trong xâu
if __name__ == '__main__':
    tc = int(input())
    d = {}
    for _ in range(tc):
        s = input().lower()
        a = s.split()
        date = a[-1]
        email = a[-2]
        for i in range(0, len(a)-2):
            email += a[i][0]
        if email in d:
            d[email] += 1
            print(email, d[email], '@xyz.edu.vn', sep = '')
        else:
            d[email] = 1
            print(email + '@xyz.edu.vn')
        date = date.split('/')
        for x in date:
            print(int(x), end='')
        print()
        