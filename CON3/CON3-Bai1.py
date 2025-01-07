n = int(input())
for i in range(n+1):
    print(i, end = ' ')
print()
for i in range(n,-1,-1):
    print(i, end = ' ')
print()
for i in range(0, n+1, 2):
    print(i, end = ' ')
print()
for i in range(1, n+1, 2):
    print(i, end = ' ')
print()
for i in range(0,n,4) :
    print(i, end = ' ')
print()
for i in range(0,n):
    print(chr(97+i), end = ' ')
print()
for i in range(122-n+1, 123):
    print(chr(i), end = ' ')
print()