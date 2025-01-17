#Ký tự xuất hiện ở 2 xâu
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    set1 = set(s1)
    set2 = set(s2)
    #xâu s1 ko xuất hiện trong s2
    print(' '.join(sorted(set1.difference(set2))))
    #Xâu s2 ko xuất hiện trong s1
    print(' '.join(sorted(set2.difference(set1))))