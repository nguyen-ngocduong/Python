#liệt kê các từ khác nhau trong xâu 
if __name__ == '__main__':
    s = input()
    tmp = s.split()
    s1 = set(tmp)
    print(' '.join(sorted(set(tmp))))
    for x in tmp:
        if x in s1:
            print(x, end = ' ')
            s1.remove(x)