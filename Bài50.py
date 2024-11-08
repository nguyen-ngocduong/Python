#Viết hàm ktra số nguyên tố
def kt_snt(a) :
    if a > 1: 
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                return False
        return True
    return False
x = int(input("Nhập số nguyên: "))
if kt_snt(x) :
    print("Yes")
else :
    print("No")