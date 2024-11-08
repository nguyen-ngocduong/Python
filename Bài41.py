# Nhập vào số nguyên dương a, nếu nhập số âm thì yêu cầu nhập lại cho đến khi người dùng nhập đúng số dương. Nếu người dùng nhập đúng số dương thì in ra “Bạn nhập đúng quy tắc”
a = int(input("Nhập số nguyên dương : "))
while a < 0 : 
    print("Nhập lại số dương.")
    a = int(input("Nhập số nguyên dương : "))
print("Nhập đúng!")