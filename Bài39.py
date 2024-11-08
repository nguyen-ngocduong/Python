#Nhập vào số nguyên dương a, kiểm tra xem a có phải là số nguyên tố hay không
def kt_snt(x) :
    if x > 1 :
        for i in range (2,int(x**(0.5))+1):
            if x % i == 0 :
                return False
        return True
    else :
        return False   
a = int(input("Nhập số nguyên dương a: "))  
if kt_snt(a) :
    print("Nó là số nguyên tố")
else :
    print("Không!")    