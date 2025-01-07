tc = int(input())
for _ in range(tc):
    c = input()
    if c == 'z' or c == 'Z':
        print('a')
    else:
        tmp = ord(c)
        tmp += 1
        print(chr(tmp).lower())