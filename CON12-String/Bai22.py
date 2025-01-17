#Tập từ riêng của 2 xâu
if __name__ == '__main__':
    s1 = input().lower()
    a1 = s1.split()
    s2 = input().lower()
    a2 = s2.split()
    set1,set2 = set(a1),set(a2)
    giao = set1.difference(set2)
    for x in sorted(giao):
        print(x, end = ' ')