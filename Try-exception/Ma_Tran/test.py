#Tinh tong tung hang cua ma tran
n = int(input("Nhap bac cua ma tran: "))
ma_tran = []
for i in range(n):
    hang = []
    for j in range(n):
        a = int(input())
        hang.append(a)
    ma_tran.append(hang)
# for i in range(n):
#     tong = 0
#     for j in range(n):
#         tong += ma_tran[i][j]
#     print(f"Tong cua hang {i} la : {tong}")
# TINH TONG TUNG COT CUA MA TRAN
# for j in range(n):
#     tong = 0
#     for i in range(n):
#         tong += ma_tran[i][j]
#     print(f"Tong cua cot {j} la : {tong}")
#Hay cho biet ma tran co phai la ma tran tam giac tren khong
tam_giac_tren = False
for i in range(n):
    for j in range(i+1, n):
        if ma_tran[i][j] != 0:
            tam_giac_tren = True
            break
if tam_giac_tren:
    print("Ma tran khong phai la ma tran tam giac tren")
else:
    print("Ma tran la ma tran tam giac tren")

#tim max cac phan tu tren duong cheo chinh
duong_cheo_chinh = []
for i in range(n):
    for j in range(n):
        duong_cheo_chinh.append(ma_tran[i][i])
print(f"Max tren duong cheo chinh la: {max(duong_cheo_chinh)}")