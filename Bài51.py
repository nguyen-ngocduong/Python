#Viết hàm đưa vào 1 số nguyên a, kiểm tra xem a có phải là số Armstrong hay không VD: 153 = 1^3 +5^3 +3^3
def armstrong(a) :
    str_a = str(a)
    len_a = len(str_a)
    sum = 0
    for char in str_a :
        sum += int(char)**len_a
    return sum == a
x = int(input("Nhập số nguyên : "))
if armstrong(x) :
    print("Yes")
else:
    print("No")