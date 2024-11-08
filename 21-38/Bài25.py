# Nhập ngày/tháng/năm của ngày sinh và hiện tại, tính tổng số ngày từ ngày sinh đến hiện tại 
import time
Nhap_ngay_sinh = input("Nhập ngày sinh của bạn: ")
Nhap_tg_hien_tai = input("Nhập thời điểm hiện tại: ")
Nhap_ngay_sinh = time.strptime(Nhap_ngay_sinh,'%d/%m/%Y')
Nhap_tg_hien_tai = time.strptime(Nhap_tg_hien_tai,'%d/%m/%Y')
# sử dụng time.mktime để tính toán
t1 = int(time.mktime(Nhap_ngay_sinh)) # timestamp tính theo giây
t2 = int(time.mktime(Nhap_tg_hien_tai))
x = int((t2 - t1)/(24*60*60))
print("Tổng số ngày là: ",x)