#Xâu pangram
#Ký tự xuất hiện nhiều nhất trong xâu
if __name__ == '__main__':
    s = input()
    s = s.lower()
    tmp = set(s)
    if len(tmp) == 26:
        print('YES')
    else:
        print('NO')