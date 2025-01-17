#Số lớn nhất, nhỏ nhất
#số có m chữ số và tổng bằng s
if __name__ =='__main__':
    m,s = map(int, input().split())
    lon,be = [0]*m, [0]*m
    if s > 9*m and (s==0 and m > 1):
        print('NOT FOUND')
    else:
        t = s
        # xét mảng lớn
        for i in range(m):
            if s >= 9:
                lon[i] = 9
                s -= 9
            else:
                lon[i] = s
                s = 0
        # xét mảng bé
        t -= 1 # đảm bảo chữ số đầu tiên luôn có 1 giá trị
        for i in range(m-1, 0, -1):
            if t >= 9:
                be[i] = 9
                t -= 9
            else:
                be[i] = t
                t = 0
        be[0] = t+1
        for x in be:
            print(x, end = '')
        print()
        for x in lon:
            print(x, end='')