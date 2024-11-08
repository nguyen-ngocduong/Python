#Viết hàm đưa vào 1 list số nguyên, tìm và trả về vị trí có giá trị lớn nhất trong list
def find_max(numbers) : # numbers : một danh sách các số đầu vào
    so_lon_nhat = 0
    for i in range (1, len(numbers)):
        if numbers[i] > numbers[so_lon_nhat]:
            so_lon_nhat = i
    return so_lon_nhat
n = list(map(int, input("Nhập các giá trị nguyên: ").split()))
so_max = find_max(n)
print(f"Vị trí có giá trị lớn nhất trong list là {so_max} với giá trị {n[so_max]}")