#Số nguyên tố
from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n% i == 0:
            return False
    return True
f1 = open('logs/Input3.txt','r')
f2 = open('logs/output3.txt', 'w')
a = list(map(int, f1.read().split()))
a.sort()
for x in a:
    if snt(x):
        f2.write(str(x) + ' ')

