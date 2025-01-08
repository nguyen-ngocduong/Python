#kiểm tra chữ số chẵn
def check(n):
    if n < 10:
        if n% 2 == 0:
            return 1
        else:
            return 0
    else:
        if n%2 == 1:
            return 0
        else: 
            return check(n//10)
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        if check(n):
            print("YES")
        else : print("NO")
    print()