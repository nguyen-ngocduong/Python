#Nhập vào n. Tính S = 1 + 2 + 3 + 4 + … + n
n = int(input("Nhập số nguyên n: "))
s = 0
for i in range(n+1):
    s += i
print(f"S = 1 + 2 + 3 + ... + {n} = ",s)