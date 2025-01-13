#Số nhỏ nhất
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(a.count(min(a)))