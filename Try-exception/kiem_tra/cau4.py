dsCuaHang = [
{
 "maCH": "CH01",
 "tenCH": "Cửa hàng A",
 "sanPham": [
 {"tenSP": "Sữa tươi", "loai": "Thực phẩm", "gia": 25000, "soLuong": 50},
 {"tenSP": "Bánh mì", "loai": "Thực phẩm", "gia": 12000, "soLuong": 100}
 ]
},
{
 "maCH": "CH02",
 "tenCH": "Cửa hàng B",
 "sanPham": [
 {"tenSP": "Nước ngọt", "loai": "Đồ uống", "gia": 15000, "soLuong": 200},
 {"tenSP": "Bánh quy", "loai": "Thực phẩm", "gia": 30000, "soLuong": 80}
 ]
}
]

def lk_sp_gia_lon_hon(lst_cua_hang, x):
    """
    Liệt kê tất cả sản phẩm có giá lớn hơn x (x nhập từ bàn phím)
    """
    lst_tm = []
    for cua_hang in lst_cua_hang:
        for sp in cua_hang["sanPham"]:
            if sp["gia"] > x:
                lst_tm.append(sp)
    return lst_tm

def them_sp_vao_cua_hang_ma(lst_cua_hang, ten_sp, loai, gia,so_luong, y):
    """
    Thêm một sản phẩm mới vào cửa hàng có mã là y (y nhập từ bàn phím).
    """
    for cua_hang in lst_cua_hang:
        if cua_hang["maCH"] == y:
            cua_hang["sanPham"].append({"tenSP": ten_sp, "loai": loai, "gia": gia, "soLuong": so_luong})
    return lst_cua_hang

def cap_nhat(lst_cua_hang, z,y, so_luong_new):
    """
    Cập nhật số lượng (soLuong) cho sản phẩm có tên là z trong cửa hàng y (z, y, số lượng nhập từ bàn phím).
    """
    check = False
    for cua_hang in lst_cua_hang:
        if cua_hang["maCH"] == y:
            for sp in cua_hang["sanPham"]:
                if sp["tenSP"] == z:
                    check = True
                    sp["soLuong"] = so_luong_new
    if check == False:
        return f"Khong co san pham nao ten {z} trong cua hang {y}"
    else:
        return lst_cua_hang
    
if __name__ == "__main__":
    x = int(input("Nhap gia dieu kien: "))
    print(lk_sp_gia_lon_hon(lst_cua_hang= dsCuaHang, x = x))
    ten_sp = input("Nhap ten sp can them: ")
    loai = input("Nhap  loai: ")
    gia = int(input("Nhap gia: "))
    so_luong = int(input("Nhap so luong: "))
    y = input("Nhap ma cua hang: ")
    print(them_sp_vao_cua_hang_ma(dsCuaHang, ten_sp, loai, gia, so_luong, y))
    y1 = input("Nhap ma cua hang: ")
    z = input("Nhap ten sp: ")
    so_luong_new = int(input("Nhap  so luong moi: "))
    print(cap_nhat(dsCuaHang, z, y, so_luong_new))