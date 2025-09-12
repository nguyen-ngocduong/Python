# try:
#     print("Xin chao")
#     lst = [3,5]
#     print(lst + 9)
#     print(10/0)
# except Exception as e:
#     print("Co loi xay ra:", e)
# finally:
#     print("Ket thuc chuong trinh")
import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# Tạo sơ đồ tư duy bằng cách sử dụng sơ đồ cây đơn giản (mindmap thủ công)
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis("off")

# Chủ đề trung tâm
ax.text(0.5, 0.9, "Phương pháp phát hiện vấn đề nghiên cứu", 
        ha="center", va="center", fontsize=14, fontweight="bold", bbox=dict(facecolor="lightblue", edgecolor="black", boxstyle="round,pad=0.5"))

# Các nhánh chính
branches = [
    ("1. Tranh luận khoa học\n(Ví dụ: Kim Tự Tháp - dốc thẳng hay xoắn ốc?)", 0.15, 0.7),
    ("2. Nghĩ ngược quan niệm\n(Ví dụ: Học online có lợi ích gì?)", 0.85, 0.7),
    ("3. Khó khăn thực tế\n(Ví dụ: Học online ở nông thôn thiếu mạng)", 0.15, 0.5),
    ("4. Lời phàn nàn từ người ngoài\n(Ví dụ: Học online gây đau mắt)", 0.85, 0.5),
    ("5. Điểm yếu nghiên cứu trước\n(Ví dụ: Ít phân tích yếu tố tâm lý)", 0.15, 0.3),
    ("6. Câu hỏi ngẫu nhiên\n(Ví dụ: Học sinh ít bật camera)", 0.85, 0.3),
]

# Vẽ các nhánh
for text, x, y in branches:
    ax.text(x, y, text, ha="center", va="center", fontsize=11,
            bbox=dict(facecolor="lightyellow", edgecolor="black", boxstyle="round,pad=0.5"))
    ax.annotate("", xy=(x, y+0.05), xytext=(0.5, 0.87),
                arrowprops=dict(arrowstyle="-|>", color="gray", lw=1.5))

plt.tight_layout()
plt.show()
