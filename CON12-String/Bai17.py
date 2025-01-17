# Chuẩn hóa tên 2
if __name__ == '__main__':
    s = input()
    a = s.split()
    a[-1] = a[-1].upper()
    for i in range(0, len(a)-1):
        a[i] = a[i].title()
    for i in range(0, len(a)-1):
        if i != len(a)-2:
            print(a[i], end = ' ')
        else: print(a[i], end =', ')
    print(a[-1])
    print(a[-1], end=', ')
    print(' '.join(a[0:-1]))
