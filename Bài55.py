year = int(input("Nhập năm: "))
if year % 4 == 0 and year % 100 != 0 :
    print("Năm %d là năm nhuận" %year)
elif year % 400 == 0 :
    print("Năm %d là năm nhuận" %year)
else :
    print("Không phải năm nhuận")