#Từ xuất hiện nhiều nhất, ít nhất
# Tần suất các từ xuất hiện trong xâu
if __name__ == '__main__':
    s = input()
    a = s.split()
    d = {}
    min_fre, max_fre = 10**18, -1
    for x in a:
        if x in d:
            d[x] += 1
        else : d[x] = 1
    res1, res2 = '',''
    for alpha, fre in sorted(d.items()):
        if fre >= max_fre:
            max_fre = fre
            res1 = alpha
        elif fre <= min_fre:
            min_fre = fre
            res2 = alpha
    print(res1, max_fre)
    print(res2, min_fre)