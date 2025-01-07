a,b = map(int, input().split())
tong = a+b
hieu = a - b
tich = a*b
if b != 0:
    thuong = a/b
    print("%.4f" %thuong)
else: print("INVALID")
print(tong, hieu, tich)
