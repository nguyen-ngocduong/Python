a,b = map(int, input().split())
res1 = (a // b) * b
print(res1)
if a%b == 0:
    print(a)
else: print((a // b) * b + b)