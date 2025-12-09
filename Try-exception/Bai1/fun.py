def cau1(dsCuaHang, x):
    lst = []
    for cuahang in dsCuaHang:
        for sanpham in cuahang["sanPham"]:
            if sanpham["gia"] < x:
                lst.append(sanpham["ten"])
    return lst 
def cau2(dsCuaHang, tukhoa):
    lst = []
    for cuahang in dsCuaHang:
        for sanpham in cuahang["sanPham"]:
            if tukhoa.lower() in sanpham["ten"].lower():
                lst.append(cuahang)
    return lst
def cau3(dsCuaHang):
    lst = []
    for cuahang in dsCuaHang:
        tong = 0
        for sanpham in cuahang["sanPham"]:
            tong += sanpham["tonKho"]
        lst.append({cuahang['tenCuaHang'] : tong})
    return lst
def cau4(dsCuaHang, ten, gia, tonKho ,i):
    for cuahang in dsCuaHang:
        if cuahang['id'] == i:
            cuahang["sanPham"].append({"ten" : ten, "gia": gia, "tonKho" : tonKho})
    return dsCuaHang
def cau5(dsCuaHang, gia_moi, ten_sp, i):
    for cuahang in dsCuaHang:
        if cuahang['id'] == i:
            for item in cuahang["sanPham"]:
                if item["ten"] == ten_sp:
                    item["gia"] = gia_moi
    return dsCuaHang
def cau6(dsCuaHang, ten_sp, i):
    for cuahang in dsCuaHang:
        if cuahang['id'] == i:
            for item in cuahang["sanPham"]:
                if item["ten"] == ten_sp:
                    cuahang["sanPham"].remove(item)
    return dsCuaHang
def cau7(dsCuaHang):
    max_store = None
    max_value = 0
    for cuahang in dsCuaHang:
        tong_kho = sum(item["gia"] * item["tonKho"] for item in cuahang["sanPham"])
        if tong_kho > max_value:
            max_value = tong_kho
            max_store = cuahang["tenCuaHang"]
    return {max_store: max_value}