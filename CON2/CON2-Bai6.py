n = int(input())
if n%2 == 0 :
    print('YES\n')
else: print("NO\n")
if n%3 == 0 and n%5 == 0:
    print("YES\n")
else: print("NO\n")
if n%3 == 0 and n%7 != 0 :
    print("YES\n")
else: print("NO\n")
if n%3 == 0 or n%7 == 0 :
    print("YES\n")
else: print("NO\n")
if n > 30 and n < 50 :
    print("YES\n")
else: print("NO\n")
if n >= 30 and (n%2 == 0 or n%3 == 0 or n%5 == 0):
    print("YES\n")
else: print("NO\n")
r = n%10
if n > 10 and n < 99 and (r==2 or r ==3 or r == 5 or r == 7) :
    print("YES\n")
else: print("NO\n")
if n <= 100 and n%23 == 0:
    print("YES\n");
else: print("NO\n")
if n < 10 or n > 20 :
    print("YES\n")
else: print("NO\n")
if r%3 == 0:
    print("YES\n")
else: print("NO\n")