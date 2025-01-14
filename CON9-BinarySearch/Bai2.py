#Sắp xếp theo trị tuyệt đối
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = abs)
    for x in a:
        print(x, end = ' ')