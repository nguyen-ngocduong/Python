#Ký tự xuất hiện nhiều nhất trong xâu
if __name__ == '__main__':
    s = input()
    d = {}
    min_val, max_val = 10**18, -10**18
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    res1,res2 = '',''
    # in theo thứ tự từ điển tăng dần
    b = sorted(d.items(),key = lambda x : x[0])
    for kitu, fre in b:
        if fre >= max_val:
            max_val = fre
            res1 = kitu
        elif fre <= min_val:
            min_val = fre
            res2 = kitu
    print(res1, max_val)
    print(res2, min_val)