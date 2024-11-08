# Nhập vào số nguyên dương n, đếm xem n có bao nhiêu chữ số chẵn, bao nhiêu chữ số lẻ
n = int(input("Nhập số nguyên dương n: "))
str_n = str(n)
count_chan = 0
count_le = 0
for char in str_n :
    if int(char) % 2 == 0 :
        count_chan += 1
    else :
        count_le += 1
print(count_chan)
print(count_le)        
