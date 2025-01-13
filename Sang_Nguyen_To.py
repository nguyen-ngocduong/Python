from math import *
#sử dụng kỹ thuật mảng đánh dấu
#0->10^6 p[1000001]
#B1: coi các số từ 0 -> n đều là snt
prime = [True]*1000001
#B2: Bội của 1 ssnt sẽ ko phải là snt
def sieve():
    prime[0], prime[1] = False, False  # 0 và 1 không phải số nguyên tố
    for i in range(2, isqrt(1000001) + 1):  # Lặp đến căn bậc hai của 10^6
        if prime[i]:  # Nếu i là số nguyên tố
            for j in range(i * i, 10**6 + 1, i):  # Đánh dấu các bội của i
                prime[j] = False  # Các bội của i không phải số nguyên tố

if __name__ == '__main__':
    sieve()
    for i in range(100):  # In ra các số nguyên tố từ 0 đến 99
        if prime[i]:
            print(i, end=' ')