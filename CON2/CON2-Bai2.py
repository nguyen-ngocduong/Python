a,b,c = map(int, input().split())
print(a,b,c, sep = ',')
S = a*(b+c) + b*(a+c)
print(S)
