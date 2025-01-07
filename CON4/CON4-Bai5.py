#tổ hợp chập k của n
from math import *
def tohop(n, k):
    if k < 0 or k > n:
        return 0  # Trường hợp không hợp lệ
    return factorial(n) // (factorial(k) * factorial(n - k))

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        n, k = map(int, input().split())
        print(tohop(n, k))