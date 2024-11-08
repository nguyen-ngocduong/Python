#:Dãy số fibonacci là dãy số được định nghĩa như sau: 1, 1, 2, 3, 5, 8, 13,... với số kế tiếp sẽ bằng tổng hai số trước đó
#Nhập vào A, hãy tìm số trong dãy số fibonacci lớn nhất nhưng không vượt quá A
A = int(input("Nhập số A: "))
a = 1
b = 1
while b <= A:
    print (b)
    a,b = b,a+b