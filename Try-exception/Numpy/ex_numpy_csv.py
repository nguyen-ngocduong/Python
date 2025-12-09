import numpy as np
import csv
import os

# =============================================================================
# THAO TÁC DỮ LIỆU CSV VỚI NUMPY
# =============================================================================

print("=" * 70)
print("THAO TÁC DỮ LIỆU CSV VỚI NUMPY")
print("=" * 70)

# 1. TẠO FILE CSV MẪU
print("\n1. TẠO FILE CSV MẪU")
print("-" * 40)

# Tạo dữ liệu nhân viên mẫu
nhan_vien_data = [
    ['ID', 'Ho_Ten', 'Tuoi', 'Luong', 'Phong_Ban', 'Kinh_Nghiem'],
    [1, 'Nguyen Van A', 28, 15000000, 'IT', 3],
    [2, 'Tran Thi B', 32, 18000000, 'HR', 5],
    [3, 'Le Van C', 25, 12000000, 'IT', 2],
    [4, 'Pham Thi D', 35, 22000000, 'Finance', 8],
    [5, 'Hoang Van E', 29, 16000000, 'IT', 4],
    [6, 'Vu Thi F', 31, 19000000, 'HR', 6],
    [7, 'Dao Van G', 27, 14000000, 'Marketing', 3],
    [8, 'Bui Thi H', 33, 20000000, 'Finance', 7],
    [9, 'Ngo Van I', 26, 13000000, 'IT', 2],
    [10, 'Ly Thi K', 30, 17000000, 'Marketing', 5]
]

# Ghi file CSV
with open('data/nhan_vien.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(nhan_vien_data)

print("✓ Đã tạo file 'nhan_vien.csv'")

# Tạo file dữ liệu số thuần túy
ban_hang_data = np.array([
    [1, 150, 2250000, 8.5],
    [2, 200, 3000000, 9.2],
    [3, 175, 2625000, 7.8],
    [4, 220, 3300000, 9.5],
    [5, 180, 2700000, 8.1],
    [6, 195, 2925000, 8.9],
    [7, 165, 2475000, 7.5],
    [8, 210, 3150000, 9.1],
    [9, 185, 2775000, 8.3],
    [10, 225, 3375000, 9.7]
])

# Ghi file CSV với header
header = 'Thang,So_Luong_Ban,Doanh_Thu,Danh_Gia'
np.savetxt('data/ban_hang.csv', ban_hang_data, delimiter=',', 
           header=header, comments='', fmt='%g')

print("✓ Đã tạo file 'ban_hang.csv'")

# 2. ĐỌC FILE CSV VỚI NUMPY
print("\n2. ĐỌC FILE CSV VỚI NUMPY")
print("-" * 40)

# Đọc file CSV chỉ có số (bỏ qua header)
ban_hang = np.loadtxt('data/ban_hang.csv', delimiter=',', skiprows=1)
print("Dữ liệu bán hàng:")
print(ban_hang)
print(f"Kích thước: {ban_hang.shape}")

# Đọc file CSV hỗn hợp (có cả text và số)
# Sử dụng genfromtxt với dtype object
try:
    nhan_vien = np.genfromtxt('data/nhan_vien.csv', delimiter=',', 
                             dtype=None, encoding='utf-8', names=True)
    print(f"\nDữ liệu nhân viên (10 dòng đầu):")
    for i, record in enumerate(nhan_vien[:5]):
        print(f"  {record}")
except:
    print("Lưu ý: Đọc file có text phức tạp, sẽ xử lý riêng từng cột số")

# Đọc riêng các cột số từ file nhân viên
nv_so_lieu = np.loadtxt('data/nhan_vien.csv', delimiter=',', skiprows=1, 
                        usecols=(0, 2, 3, 5))  # ID, Tuoi, Luong, Kinh_Nghiem
print(f"\nDữ liệu số của nhân viên:")
print("Cột: [ID, Tuoi, Luong, Kinh_Nghiem]")
print(nv_so_lieu)

# 3. PHÂN TÍCH DỮ LIỆU BÁN HÀNG
print("\n3. PHÂN TÍCH DỮ LIỆU BÁN HÀNG")
print("-" * 40)

# Trích xuất các cột
thang = ban_hang[:, 0]
so_luong = ban_hang[:, 1]
doanh_thu = ban_hang[:, 2]
danh_gia = ban_hang[:, 3]

print(f"Tháng: {thang}")
print(f"Số lượng bán: {so_luong}")
print(f"Doanh thu: {doanh_thu}")
print(f"Đánh giá: {danh_gia}")

# Thống kê cơ bản
print("\nTHỐNG KÊ BÁN HÀNG:")
print(f"📊 Tổng số lượng bán: {np.sum(so_luong):,.0f}")
print(f"💰 Tổng doanh thu: {np.sum(doanh_thu):,.0f} VNĐ")
print(f"📈 Doanh thu trung bình: {np.mean(doanh_thu):,.0f} VNĐ")
print(f"🔝 Doanh thu cao nhất: {np.max(doanh_thu):,.0f} VNĐ")
print(f"🔻 Doanh thu thấp nhất: {np.min(doanh_thu):,.0f} VNĐ")
print(f"⭐ Đánh giá trung bình: {np.mean(danh_gia):.2f}/10")

# Tìm tháng có doanh thu cao nhất
thang_max = thang[np.argmax(doanh_thu)]
print(f"🏆 Tháng có doanh thu cao nhất: Tháng {thang_max:.0f}")

# 4. PHÂN TÍCH DỮ LIỆU NHÂN VIÊN
print("\n4. PHÂN TÍCH DỮ LIỆU NHÂN VIÊN")
print("-" * 40)

# Trích xuất các cột số
nv_id = nv_so_lieu[:, 0]
nv_tuoi = nv_so_lieu[:, 1]
nv_luong = nv_so_lieu[:, 2]
nv_kinhnghiem = nv_so_lieu[:, 3]

print("THỐNG KÊ NHÂN VIÊN:")
print(f"👥 Tổng số nhân viên: {len(nv_tuoi)}")
print(f"🎂 Tuổi trung bình: {np.mean(nv_tuoi):.1f} tuổi")
print(f"💼 Lương trung bình: {np.mean(nv_luong):,.0f} VNĐ")
print(f"🎯 Kinh nghiệm trung bình: {np.mean(nv_kinhnghiem):.1f} năm")
print(f"💰 Lương cao nhất: {np.max(nv_luong):,.0f} VNĐ")
print(f"💸 Lương thấp nhất: {np.min(nv_luong):,.0f} VNĐ")

# 5. CÁC THAO TÁC NÂNG CAO
print("\n5. CÁC THAO TÁC NÂNG CAO")
print("-" * 40)

# Lọc dữ liệu - Nhân viên có lương > 15 triệu
nv_luong_cao = nv_so_lieu[nv_luong > 15000000]
print(f"Số nhân viên có lương > 15 triệu: {len(nv_luong_cao)}")
print(f"ID nhân viên lương cao: {nv_luong_cao[:, 0]}")

# Sắp xếp theo lương
nv_sorted = nv_so_lieu[np.argsort(nv_luong)]
print(f"\nTop 3 lương thấp nhất:")
for i in range(3):
    print(f"  ID {nv_sorted[i, 0]:.0f}: {nv_sorted[i, 2]:,.0f} VNĐ")

print(f"\nTop 3 lương cao nhất:")
for i in range(-3, 0):
    print(f"  ID {nv_sorted[i, 0]:.0f}: {nv_sorted[i, 2]:,.0f} VNĐ")

# 6. TÍNH TOÁN THỐNG KÊ NÂNG CAO
print("\n6. TÍNH TOÁN THỐNG KÊ NÂNG CAO")
print("-" * 40)

# Tương quan giữa tuổi và lương
correlation = np.corrcoef(nv_tuoi, nv_luong)[0, 1]
print(f"Tương quan tuổi-lương: {correlation:.3f}")

# Tương quan giữa kinh nghiệm và lương
correlation_exp = np.corrcoef(nv_kinhnghiem, nv_luong)[0, 1]
print(f"Tương quan kinh nghiệm-lương: {correlation_exp:.3f}")

# Percentiles
p25 = np.percentile(nv_luong, 25)
p50 = np.percentile(nv_luong, 50)  # median
p75 = np.percentile(nv_luong, 75)

print(f"\nPhân vị lương:")
print(f"  P25 (25%): {p25:,.0f} VNĐ")
print(f"  P50 (50%): {p50:,.0f} VNĐ")
print(f"  P75 (75%): {p75:,.0f} VNĐ")

# 7. GHI DỮ LIỆU ĐÃ XỬ LÝ RA FILE MỚI
print("\n7. GHI DỮ LIỆU ĐÃ XỬ LÝ")
print("-" * 40)

# Tạo báo cáo thống kê
thong_ke_ban_hang = np.array([
    ['Thong_Ke', 'Gia_Tri'],
    ['Tong_So_Luong', np.sum(so_luong)],
    ['Tong_Doanh_Thu', np.sum(doanh_thu)],
    ['TB_Doanh_Thu', np.mean(doanh_thu)],
    ['Max_Doanh_Thu', np.max(doanh_thu)],
    ['Min_Doanh_Thu', np.min(doanh_thu)],
    ['TB_Danh_Gia', np.mean(danh_gia)]
], dtype=object)

# Ghi ra file CSV
np.savetxt('data/bao_cao_ban_hang.csv', thong_ke_ban_hang, 
           delimiter=',', fmt='%s', encoding='utf-8')

# Ghi dữ liệu nhân viên lương cao
header_luong_cao = 'ID,Tuoi,Luong,Kinh_Nghiem'
np.savetxt('data/nhan_vien_luong_cao.csv', nv_luong_cao, 
           delimiter=',', header=header_luong_cao, 
           comments='', fmt='%g')

print("✓ Đã tạo file 'bao_cao_ban_hang.csv'")
print("✓ Đã tạo file 'nhan_vien_luong_cao.csv'")

# 8. XỬ LÝ DỮ LIỆU THIẾU (MISSING DATA)
print("\n8. XỬ LÝ DỮ LIỆU THIẾU")
print("-" * 40)

# Tạo dữ liệu có giá trị thiếu
du_lieu_thieu = np.array([
    [1, 25, 15000000, 3],
    [2, np.nan, 18000000, 5],
    [3, 30, np.nan, 4],
    [4, 35, 22000000, np.nan],
    [5, 28, 16000000, 6]
])

print("Dữ liệu gốc có giá trị thiếu:")
print(du_lieu_thieu)

# Kiểm tra giá trị thiếu
co_nan = np.isnan(du_lieu_thieu)
print(f"\nVị trí có giá trị thiếu:\n{co_nan}")
print(f"Tổng số giá trị thiếu: {np.sum(co_nan)}")

# Thay thế giá trị thiếu bằng giá trị trung bình
du_lieu_clean = du_lieu_thieu.copy()
for i in range(du_lieu_thieu.shape[1]):
    col = du_lieu_thieu[:, i]
    if np.any(np.isnan(col)):
        mean_val = np.nanmean(col)  # Trung bình bỏ qua NaN
        du_lieu_clean[:, i] = np.where(np.isnan(col), mean_val, col)

print(f"\nDữ liệu sau khi thay thế NaN bằng trung bình:")
print(du_lieu_clean)

# 9. KẾT HỢP NHIỀU FILE CSV
print("\n9. KẾT HỢP NHIỀU FILE CSV")
print("-" * 40)

# Tạo thêm file CSV khác
du_lieu_them = np.array([
    [11, 24, 11000000, 1],
    [12, 36, 25000000, 10],
    [13, 29, 17000000, 5]
])

np.savetxt('data/nhan_vien_them.csv', du_lieu_them, 
           delimiter=',', header='ID,Tuoi,Luong,Kinh_Nghiem',
           comments='', fmt='%g')

# Đọc và kết hợp
nv_them = np.loadtxt('data/nhan_vien_them.csv', delimiter=',', skiprows=1)
nv_ket_hop = np.vstack([nv_so_lieu, nv_them])

print(f"Dữ liệu gốc: {nv_so_lieu.shape}")
print(f"Dữ liệu thêm: {nv_them.shape}")
print(f"Dữ liệu kết hợp: {nv_ket_hop.shape}")
print(f"\nDữ liệu kết hợp:")
print(nv_ket_hop)

print("\n" + "=" * 70)
print("HOÀN THÀNH! ĐÃ THỰC HIỆN CÁC THAO TÁC CSV VỚI NUMPY")
print("Files đã tạo: nhan_vien.csv, ban_hang.csv, bao_cao_ban_hang.csv")
print("nhan_vien_luong_cao.csv, nhan_vien_them.csv")
print("=" * 70)