n = int(input())
a = list(map(int, input().split()))
lst_chan = []
for i in a:
    if i % 2 == 0:
        lst_chan.append(i)
print(max(lst_chan))
#Dem va in ra man hinh cac cap so lien tiep ma tich chia tong du 3
dem = 0
lst_tm = []
for i in range(len(a) - 1):
    tich = a[i] * a[i+1]
    tong = a[i] + a[i+1]
    if tich % tong == 3:
        dem += 1
        lst_tm.append(f"({a[i]}, {a[i+1]})")
print(lst_tm)
print(dem)
#Nhap vao so x, tinh tong cac so lon hon x
x = int(input())
tong_lon_hon_x = 0
for i in a:
    if i > x:
        tong_lon_hon_x += i
print(tong_lon_hon_x)