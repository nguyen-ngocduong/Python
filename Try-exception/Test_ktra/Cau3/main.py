from class_file import *

def dem_mau(lst_xe_may, mau):
    dem = 0
    for xe_may in lst_xe_may:
        if xe_may.get_mau() == mau:
            dem += 1
    return dem
if __name__ == "__main__":
    n,m = map(int, input().split())

    lst_oto = []
    lst_xe_may = []

    for _ in range(n):
        oto = XeOto()
        oto.nhap()
        lst_oto.append(oto)

    x = int(input("Dieu kien so cho ngoi: "))
    for oto in lst_oto:
        if oto.get_so_cho() == x:
            oto.show()
    #Tong tai trong nhung xe y cho
    y = float(input("Nhap y: "))
    tong = 0
    for oto in lst_oto:
        if oto.get_so_cho() == y:
            tong += oto.get_tai_trong()
    print(f"Tong tai trong cua oto {y} cho la: {tong}")

    for _ in range(m):
        xe_may = XeMay()
        xe_may.nhap()
        lst_xe_may.append(xe_may)
    mau = input("Nhap mau: ")
    print(dem_mau(lst_xe_may, mau))

