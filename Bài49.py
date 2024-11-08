#Viết hàm đưa vào 2 số nguyên, số nào lớn hơn thì in bảng cửu chương của số đó
def function(number1, number2) :
    n = max(number1, number2)
    for i in range(1,11) :
        print(f"{n} x {i} = {n * i}")
n1 = int(input("Nhập số thứ nhất: "))
n2 = int(input("Nhập số thứ hai : "))
function(n1, n2)