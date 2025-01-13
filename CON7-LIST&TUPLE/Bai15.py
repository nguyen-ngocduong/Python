#Số lớn nhất và số lớn thứ 2
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1], a[n-2])