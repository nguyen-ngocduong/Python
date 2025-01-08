#tìm chữ số nhỏ nhất và lớn nhất của 1 số
def findmax(n):
    if n < 10 :
        return n
    else:
        return max(n%10, findmax(n//10))
def findmin(n):
    if n < 10:
        return n
    else :
        return min(n%10, findmin(n//10))
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(findmin(n), findmax(n), end = ' ')
        print()