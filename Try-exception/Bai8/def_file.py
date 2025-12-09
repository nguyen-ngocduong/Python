from class_file import *
def dem_so_tin_chi(danh_sach_mon_hoc):
    """
    Tinh tong so tin chi cua 1 sinh vien
    """
    tong_tin_chi = 0
    for mon_hoc in danh_sach_mon_hoc:
        tong_tin_chi += mon_hoc.get_so_tc()
    return tong_tin_chi

def info_sv_dang_ky_mon(lstSV, ten_mon_hoc):
    """
    In ra cac sinh vien da dang ky mon : {ten_mon_hoc}
    """
    new_lst_sv = []
    for sinh_vien in lstSV:
        danh_sach_mon_hoc = sinh_vien.get_danh_sach_mon()
        for mon_hoc in danh_sach_mon_hoc:
            if mon_hoc.get_ten_mon() == ten_mon_hoc:
                new_lst_sv.append(sinh_vien)
    return new_lst_sv