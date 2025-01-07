tc = int(input())
for _ in range(tc):
    n = int(input())
    nam = n // 365
    n = n%365
    tuan = n // 7
    n = n%7
    ngay = n
    print(nam, tuan, ngay)