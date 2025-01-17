#Tần suất xuất hiện của ký tự
if __name__ == '__main__':
    s = input()
    d = {}
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    # in theo thứ tự từ điển tăng dần
    b = sorted(d.items(),key = lambda x : x[0])
    for alpha, fre in b:
        print(alpha, fre)
    print()
    # in theo thứ tự xuất hiện
    for alpha, fre in d.items():
        print(alpha, fre)
    print()