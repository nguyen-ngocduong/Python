#Ngôn ngữ lập trình Python
# Tần suất các từ xuất hiện trong xâu
if __name__ == '__main__':
    s = input()
    # if 'p' in s and 'y' in s and 't' in s and 'h' in s and 'o' in s and 'n' in s:
    #     print('YES')
    # else:
    #     print('NO')
    t = 'python'
    tmp = 0
    for x in s:
        if x == t[tmp]:
            tmp += 1
        if tmp == 6:
            print("YES")
            exit()
    print('NO')