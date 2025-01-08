#tổ hợp chập k của n
def tohop(n,k):
    if k == 0 or n == k:
        return 1
    else :
        return tohop(n-1, k-1) + tohop(n-1,k)
if __name__ == "__main__":
    n,k = map(int,input().split())
    print(tohop(n,k))