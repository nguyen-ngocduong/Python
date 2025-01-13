#mảng chẵn
from math import *
from sys import stdin
if __name__ == '__main__':
    a = []
    for s in stdin:
        x = list(map(int, s.split()))
        a += x
    chan, le = 0,0
    for x in a:
        if x % 2 == 0:
            chan += 1
        else :
            le += 1
    if chan == le :
        print("CHANLE")
    elif chan > le:
        print("CHAN")
    else:
        print("LE")