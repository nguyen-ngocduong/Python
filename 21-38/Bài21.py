a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
delta = b**b - 4*a*c
if delta < 0 :
    print("Phương trình vô nghiệm")
elif delta == 0:
    x = -b/(2*a)
    print("Phương trình có nghiệm kép: ",x)
else :
    x1 = (-b + delta**0.5)/(2*a)
    x2 = (-b - delta**0.5)/(2*a)
    print("Phương trình có 2 nghiệm phân biệt: x1 =", x1, "và x2 =", x2)      