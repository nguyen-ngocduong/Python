# Nhập vào số nguyên dương n, tính tổng các chữ số của n
n = int(input("Nhập số nguyên dương n: "))
sum = 0
while n > 0:
    x = n % 10
    sum += x
    n //= 10
print(sum)