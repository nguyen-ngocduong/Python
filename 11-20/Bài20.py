a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
if a == 0 :
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else :
        print("Phương trình vô nghiệm")
else :
    x = -b/a
    print("Phương trình có nghiệm là: ",x)            