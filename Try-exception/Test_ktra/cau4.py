dsLopHoc = [
 {
 "maLop": "10A1",
 "giaoVienCN": "Nguyễn Thị Mai",
 "hocSinh": [{"hoTen": "Trần Văn A", "gioiTinh": "Nam", "diemTB": 8.2, "hoatDong": ["Bóng đá","Văn nghệ"]},
 {"hoTen": "Lê Thị B", "gioiTinh": "Nữ", "diemTB": 9.1, "hoatDong": ["Học nhóm", "Cờ vua"]}]
 },

 {
 "maLop": "10A2",
 "giaoVienCN": "Phạm Văn Cường",
 "hocSinh": [
 {"hoTen": "Ngô Văn C", "gioiTinh": "Nam", "diemTB": 6.8, "hoatDong": ["Bóng rổ"]},
 {"hoTen": "Phan Thị D", "gioiTinh": "Nữ", "diemTB": 7.5, "hoatDong": ["Văn nghệ","Học nhóm"]}]
 }
]
def hoc_sinh_co_dtb_lon_hon(dsLopHoc, x):
    """
    Liệt kê tất cả học sinh có điểm trung bình lớn hơn x (x nhập từ bàn phím).
    """
    lst_hs = []
    for lop_hoc in dsLopHoc:
        for hoc_sinh in lop_hoc["hocSinh"]:
            if hoc_sinh["diemTB"] > x:
                lst_hs.append(hoc_sinh)
    return lst_hs

def them_hoc_sinh_co_ma(dsLopHoc, x, name, gioi_tinh, diem, hoat_dong):
    """
    Thêm một học sinh mới vào lớp có mã là x (x nhập từ bàn phím).
    """
    for lop_hoc in dsLopHoc:
        if lop_hoc["maLop"] == x:
            lop_hoc["hocSinh"].append({"hoTen": name, "gioiTinh": gioi_tinh, "diemTB": diem, "hoatDong": hoat_dong})
    return dsLopHoc
def cap_nhat(dsLopHoc,x,y,diem_moi):
    """
    Cập nhật điểm trung bình (dtb) cho học sinh có tên là x trong lớp y. Với dtb, x, y nhập từ bàn phím
    """
    for lop_hoc in dsLopHoc:
        if lop_hoc["maLop"] == y:
            for hoc_sinh in lop_hoc["hocSinh"]:
                if hoc_sinh["hoTen"] == x:
                    hoc_sinh["diemTB"] = diem_moi
    return dsLopHoc

if __name__ == "__main__":
    nguong_tb = float(input("Nhap nguong diem trung binh: "))
    print(hoc_sinh_co_dtb_lon_hon(dsLopHoc, nguong_tb))
    ma_lop_1 = input("Nhap ma lop cho cau b: ")
    name = input("Nhap ten hs can them: ")
    gioi_tinh = input("Nhap gioi tinh: ")
    diem_tb = float(input("Nhap diem: "))
    n = int(input("Nhap so hoat dong: "))
    hoat_dong = []
    for i in range(n):
        hd = input(f"Nhap hoat dong {i + 1}: ")
        hoat_dong.append(hd)
    print(them_hoc_sinh_co_ma(dsLopHoc, ma_lop_1, name, gioi_tinh, diem_tb, hoat_dong))
    x = input("Nhap ten hs: ")
    y = input("Nhap ma lop: ")
    diem_moi = float(input(f"Nhap diem moi cho hs {x} lop {y}: "))
    print(cap_nhat(dsLopHoc, x,y,diem_moi))