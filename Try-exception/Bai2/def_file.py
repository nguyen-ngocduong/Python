from class_file import *
# Tinh tong so tin chi cua tat ca cac hoc ky
# def tinh_tong_so_tc(danh_sach_hoc_ky):
#     tong_so_tc = 0
#     for hoc_ky in danh_sach_hoc_ky:
#         danh_sach_mon_hoc = hoc_ky.get_danh_sach_mon_hoc()
#         for mon_hoc in danh_sach_mon_hoc:
#             tong_so_tc += mon_hoc.get_so_tc()
#     return tong_so_tc

#Tim hoc ky co nhieu tin chi nhat
def tim_hoc_ky_nhieu_tc(danh_sach_hoc_ky):
    max_so_tc = 0
    hoc_ky_nhieu_tc = None
    for hoc_ky in danh_sach_hoc_ky:
        so_tc_hien_tai = 0
        danh_sach_mon_hoc = hoc_ky.get_danh_sach_mon_hoc()
        for mon_hoc in danh_sach_mon_hoc:
            so_tc_hien_tai += mon_hoc.get_so_tc()
        if so_tc_hien_tai > max_so_tc:
            max_so_tc = so_tc_hien_tai
            hoc_ky_nhieu_tc = hoc_ky
    return hoc_ky_nhieu_tc