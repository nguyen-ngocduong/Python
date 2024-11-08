animal = ["Ty","Suu","Dan","Mao","Thin","Tyj","Ngo","Mui","Than","Dau","Tuat","Hoi"]
year = int(input("Nhập năm: "))
n = animal[(year -4)%12]
print("Là năm con: ", n)