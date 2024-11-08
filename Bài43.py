# Nhập vào một dãy số nguyên, ngưng nhập khi người dùng nhập -1.
#Sau khi nhập xong, in số lớn nhất, số nhỏ nhất trong những số vừa nhập
a = int(input("Nhập số nguyên a: "))
min_a = a
max_a = a
while a != -1 :
    if a > max_a :
        max_a = a
    if a < min_a :
        min_a = a
    a = int(input("Nhập số nguyên a: "))
print("Số lớn nhất: ", max_a)
print("Số nhỏ nhất: ", min_a)