toan = float(input("Nhập điểm toán: "))
van = float(input("Nhập điểm văn: "))
anh = float(input("Nhập điểm anh: "))
gpa = (toan + van + anh)/3
if gpa >= 8 and toan>=8 or van>=8 or anh>=8 and toan>=6.5 and van>=6.5 and anh>=6.5:
    print("Học sinh giỏi")
elif gpa >= 6.5 and toan>=6.5 or van >= 6.5 and toan >= 5 and van >= 5 and anh >= 5 :
    print("Học sinh khá")
elif gpa >= 5 and toan >= 5 or van >=5 and toan >= 3.5 and van >= 3.5 and anh >= 3.5:
    print("Học sinh trung bình")
elif gpa >= 3.5 and (toan >= 3.5 or van >= 3.5 or anh >= 3.5) and toan >= 2 and van >= 2 and anh >= 2:
    print("Học sinh yếu") 
else :
    print("Học sinh kém")  