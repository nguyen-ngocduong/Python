#Tìm kiếm nhị phân biến đổi
def ham1(a,l,r,x): #Tìm vị trí xuất hiện đầu tiên
    res = -1
    while l <= r:
        m = (l+r) // 2
        if a[m] == x:
            res = m
            r = m - 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res
def ham2(a,l,r,x): # tìm vị trí xuất hiện cuối cùng
    res = -1
    while l <= r:
        m = (l+r) // 2
        if a[m] == x:
            res = m
            l = m + 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res

def ham3(a,l,r,x): #tìm vị trí ptu >= đầu tiên xuất hiện
    res = -1
    while l <= r:
        m = (l+r) // 2
        if a[m] >= x :
            res = m
            r = m - 1
        else:
            l = m + 1
    return res
def ham4(a,l,r,x): #tìm vị trí ptu > đầu tiên trong mảng
    res = -1
    while l <= r :
        m = (l+r) // 2
        if a[m] > x:
            res = m
            r = m - 1
        else :
            l = m + 1
    return res
def ham5(a, l, r, x):#tìm số lần xuất hiện của ptu
    tmp1 = ham1(a, l, r, x)
    tmp2 = ham2(a, l, r, x)
    if tmp1 == -1 :
        return 0
    elif tmp1 == tmp2:
        return 1
    else:
        return tmp2 - tmp1 + 1
    
if __name__ == '__main__':
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    res1, res2, res3, res4, res5 = ham1(a, 0, len(a)-1, x), ham2(a, 0, len(a)-1, x), ham3(a, 0, len(a)-1, x), ham4(a, 0, len(a)-1, x), ham5(a, 0, len(a)-1, x)
    print(res1, res2, res3, res4, res5, end = ' ')