import random 
print("Trò chơi kéo-búa-bao bắt đầu")
print("1.Kéo")
print("2.Búa")
print("3.Bao")
ban_chon = int(input("Mời bạn chọn (1/2/3): "))
may_chon = random.randint(1,3)
print("Máy chọn: ",may_chon)
if (ban_chon == 1 and may_chon == 3) or (ban_chon == 2 and may_chon == 1) or (ban_chon == 3 and may_chon == 2) :
    print("Bạn là người thắng cuộc!")
elif (ban_chon == may_chon) :
    print("Bạn và máy hòa!")
else :
    print("Bạn là người thua cuộc!")