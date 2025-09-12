from fun import *

dsCuaHang = [
    {
        "id": 1,
        "tenCuaHang": "Điện Máy Xanh",
        "diaChi": "Quận 1, TP.HCM",
        "sanPham": [
            {"ten": "Tivi Samsung", "gia": 12000000, "tonKho": 10},
            {"ten": "Tủ lạnh LG", "gia": 9000000, "tonKho": 5}
        ]
    },
    {
        "id": 2,
        "tenCuaHang": "Thế Giới Di Động",
        "diaChi": "Quận 3, TP.HCM",
        "sanPham": [
            {"ten": "iPhone 14", "gia": 25000000, "tonKho": 15},
            {"ten": "Tai nghe AirPods", "gia": 4500000, "tonKho": 20}
        ]
    }
]
print(cau1(dsCuaHang, x = 10000000))
print(cau2(dsCuaHang, tukhoa="Tivi Samsung"))
print(cau3(dsCuaHang))
print(cau4(dsCuaHang, ten = "Laptop Dell", gia = 15000000, tonKho = 8 ,i=1))
print(cau5(dsCuaHang, gia_moi = 20000000, ten_sp = "iPhone 14", i=2))
print(cau6(dsCuaHang, ten_sp = "Tivi Samsung", i=1))
print(cau7(dsCuaHang))  
