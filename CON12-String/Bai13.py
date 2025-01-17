# Tần suất các từ xuất hiện trong xâu
if __name__ == '__main__':
    s = input()
    a = s.split()
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else: d[x] = 1
    #in theo thứ tự xuất hiện
    for alpha, fre in d.items():
        print(alpha, fre, end = '\n')
    #Sắp xếp theo thứ tự từ điển
    tmp = sorted(d.items())
    for alpha, fre in tmp :
        print(alpha, fre, end = '\n')