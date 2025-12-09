from math import *
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
a = list(map(int, input().split()))
#Tìm giá trị âm nhỏ nhất trong dãy
am_nho_nhat = None
for i in a:
    if i < 0:
        if am_nho_nhat is None or i < am_nho_nhat:
            am_nho_nhat = i
if am_nho_nhat is not None:
    print(am_nho_nhat)
else: print(0)
#Đếm và in ra màn hình các phần tử là số nguyên tố.
lst_snt = []
for i in a:
    if isPrime(i):
        lst_snt.append(i)
print(len(lst_snt))
print(*lst_snt)
#Nhập vào 1 số nguyên dương k, tìm và in ra tất cả các số trong dãy chia hết cho k
lst_tm_dk = []
k = int(input())
for i in a:
    if i % k == 0:
        lst_tm_dk.append(i)
print(*lst_tm_dk)
#Sắp xếp dãy theo thứ tự giảm dần và in kết quả ra màn hình
a.sort(reverse=True)
print(*a)