from class_file import *

def sap_xep_theo_snct(nhan_vien):
    return nhan_vien.get_snct()

def sap_xep_theo_tien_luong(nhan_vien, luong_cb, bonus):
    return nhan_vien.get_tien_luong(luong_cb, bonus)
