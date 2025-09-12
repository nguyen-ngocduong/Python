from class_file import *

def ten_cty_pmen_tm_dk(lstctypm, nam_thanh_lap, so_ltv):
    """
    Liet ke cac cong ty thanh lap sau nam {nam_thanh_lap};
    co so luong thanh vien > {so_ltv}
    """
    new_lst = []
    for cty in lstctypm:
        if cty.get_ntl() > nam_thanh_lap and cty.get_sltv() > so_ltv:
            new_lst.append(cty)
    return new_lst

def ten_cty_vt_tm_dk(lstctyvt, nam_thanh_lap, so_oto):
    """
    Liet ke cac cong ty thanh lap sau nam {nam_thanh_lap};
    co so luong oto > {so_oto}
    """
    new_lst = []
    for cty in lstctyvt:
        if cty.get_ntl() < nam_thanh_lap and cty.get_soto() <= so_oto:
            new_lst.append(cty)
    return new_lst