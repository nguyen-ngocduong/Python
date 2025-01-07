n = int(input())
cnt = 0
if n == 0 :
    print(1)
else:
    while n != 0:
        cnt+=1
        n //= 10
    print(cnt)