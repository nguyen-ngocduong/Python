from class_file import *

n = int(input("Nhap so luong xe con: "))
list_xe = []
for _ in range(n):
    xe = XeCon()
    xe.nhap()
    list_xe.append(xe)
print("\nCac xe con co so cho ngoi <= 5 va trong tai <= 1 tan:")
for xe in list_xe:
    if xe.get_so_cho() <= 5 and xe.get_weight() <= 1:
        xe.show()
        print()