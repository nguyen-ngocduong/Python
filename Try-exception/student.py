class Student:
    def __init__(self, id = "", name = "", age = 1, grade = 1.0):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__grade = grade
    def nhap(self):
        self.__id = input("Nhap ma sinh vien: ")
        self.__name = input("Nhap ho ten sinh vien: ")
        self.__age = int(input("Nhap tuoi: "))
        self.__grade = float(input("Nhap gpa: "))
    def show(self):
        print(f"{self.__id} - {self.__name} - {self.__age} - {self.__grade}")
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_grade(self):
        return self.__grade
def xoa_sinh_vien(lstStudent, id_sv_bi_xoa):
    for sv in lstStudent:
        if sv.get_id() == id_sv_bi_xoa:
            lstStudent.remove(sv)
            break
    return lstStudent
def find_student(lstStudent, ten):
    output = []
    for sv in lstStudent:
        if ten in sv.get_name():
            output.append(sv)
    return output
def tinh_diem_tb(lstStudent):
    diem = []
    for sv in lstStudent:
        diem.append(sv.get_grade())
    return sum(diem) / len(diem)
n = int(input("Nhap so luong sinh vien: "))
lstStudent = []
for _ in range(n):
    sv = Student()
    sv.nhap()
    lstStudent.append(sv)
for sv in lstStudent:
    sv.show()
id_sv_bi_xoa = input("Nhap id can xoa: ")
lst_xoa_sv = xoa_sinh_vien(lstStudent, id_sv_bi_xoa)
for sv in lst_xoa_sv:
    sv.show()
ten_can_tim = input("Nhap ten can tim: ")
ten_thoa_man = find_student(lstStudent, ten_can_tim)
for sv in ten_thoa_man:
    sv.show()
print(f"Diem trung binh ca lop: {tinh_diem_tb(lstStudent)}")