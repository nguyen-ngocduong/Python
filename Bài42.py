# Nhập vào A, tìm n nhỏ nhất sao cho
# sum = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n > A
a = float(input("Nhập số a: "))
n = 1
sum = 0
while sum <= a :
    sum += 1/n
    n += 1
print(n-1)