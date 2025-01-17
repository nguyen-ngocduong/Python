#Đếm số loại ký tự trong xâu
if __name__ == '__main__':
    s = input()
    kytu, so, special = 0, 0, 0
    for x in s:
        if x.isdigit():
            so += 1
        elif x.isalpha():
            kytu += 1
        else:
            special += 1
    print(kytu,so,special, end = ' ')