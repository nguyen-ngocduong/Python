#Sắp xếp các từ trong xâu
if __name__ == '__main__':
    s = input()
    t = s.split()
    t.sort()
    #in theo thứ tự từ điển
    for x in t:
        print(x, end = ' ')
    print()
    # in theo độ dài từ điển
    t.sort(key = lambda x : (len(x), x))
    print(' '.join(t))