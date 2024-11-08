#Nhập vào số nguyên dương a và b, in toàn bộ ước chung của a và b
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
uoc_chung = []
Min = min(a, b)
for i in range (1,Min+1) :
    if a%i == 0 and b%i == 0 :
        uoc_chung.append(i)
print("Ước chung của a và b là: ",uoc_chung)        