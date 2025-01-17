#Ký tự xuất hiện ở cả 2 xâu
#Ký tự xuất hiện nhiều nhất trong xâu
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    set1 = set(s1)
    set2 = set(s2)
    #Tập giao
    print(' '.join(sorted(set1.intersection(set2))))
    #Tập hợp
    print(' '.join(sorted(set1.union(set2))))