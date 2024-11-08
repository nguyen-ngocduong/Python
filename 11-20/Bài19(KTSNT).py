def kt_snt(x):
    if x > 1:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False

a = int(input("Nhập số nguyên a: "))
if kt_snt(a):
    print("Đây là số nguyên tố")
else:
    print("Đây không phải là số nguyên tố")      