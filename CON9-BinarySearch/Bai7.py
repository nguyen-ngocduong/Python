#Trộn 2 dãy
if __name__ == '__main__':
    n,m = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    i,j = 0,0
    while i < n and j < n:
        if b[i] <= c[j]:
            print("b", i+1, sep = '', end = ' ')
            i += 1
        else:
            print("c", j+1, sep = '', end = ' ')
            j += 1
    while i < n:
        print('b', i+1, sep = '', end = ' ')
        i += 1
    while j < m:
        print('c', j + 1, sep = '', end = ' ')
        j += 1