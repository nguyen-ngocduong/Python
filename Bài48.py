subjects = ['Toan', 'Ly', 'Hoa', 'Van', 'Anh']
# Tạo danh sách chứa các điểm học sinh
student_scores = []
# Nhập vào các điểm cho 5 môn học cho từng học sinh
num_students = int(input("Nhap so luong hoc sinh: "))
for i in range(num_students):
    scores = []
    name = input("Nhap ten hoc sinh: ")
    scores.append(name)
    for subject in subjects:
        midterm = float(input("Nhap diem mieng {}: ".format(subject)))
        quarter = float(input("Nhap diem 15 phut {}: ".format(subject)))
        fullterm = float(input("Nhap diem 1 tiet {}: ".format(subject)))
        exam = float(input("Nhap diem thi {}: ".format(subject)))
        avg_score = (midterm + quarter + fullterm * 2 + exam * 3) / 7
        scores.append(avg_score)
    student_scores.append(scores)

# Sắp xếp danh sách theo điểm trung bình giảm dần
student_scores.sort(key=lambda x: x[5], reverse=True)

# Cập nhật xếp loại cho mỗi học sinh
for i in range(len(student_scores)):
    student_scores[i].append(i + 1)

# In ra bảng điểm
print("{:<20} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Ten", "Toan", "Ly", "Hoa", "Van", "Anh", "Xep Loai"))
for student in student_scores:
    print("{:<20} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<10d}".format(*student))

