#tính tổng chữ số chẵn lẻ
def tongchan(n):
    if n < 10:
        if n % 2 == 0:
            return n
        else:
            return 0
    else:
        if n%2 == 0:
            return n%10 + tongchan(n//10)
        else:
            return tongchan(n//10)
def tongle(n):
    if n < 10 :
        if n % 2: 
            return n
        else :
            return 0
    else:
        if n%2 == 1:
            return n % 10 + tongle(n // 10)
        else:
            return tongle(n//10)
if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        n = int(input())
        print(tongchan(n), tongle(n), end = ' ')
        print()