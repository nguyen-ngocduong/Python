# đếm số lượng chữ số của n sử dụng đệ quy
def demchuso(n):
    if n < 10 :
        return 1
    else:
        return 1 + demchuso(n // 10)
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(demchuso(n))