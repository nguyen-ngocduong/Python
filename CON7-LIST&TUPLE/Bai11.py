#Liệt kê và đếm số fibo
fibo = [0]*100
def khoitao():
    fibo[0] = 0
    fibo[1] = 1
    for i in range(2, 99):
        fibo[i] = fibo[i-1]+fibo[i-2]

if __name__ == '__main__':
    khoitao()
    n = int(input())
    a = list(map(int, input().split()))
    check = False
    for x in a:
        if x in fibo:
            print(x, end = ' ')
            check = True
    if not check :
        print('NONE')
