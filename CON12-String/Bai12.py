#Sắp xếp các từ trong xâu 2
def check(s):
    rev = s[::-1]
    return rev == s
if __name__ == '__main__':
    s = input()
    a = s.split()
    tmp = set({})
    b = []
    for x in a:
        if check(x) and x not in tmp:
            b.append(x)
            tmp.add(x)
    b.sort(key = lambda x : len(x))
    print(' '.join(b))