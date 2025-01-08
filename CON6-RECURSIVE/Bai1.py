def S(n):
    if n == 0:
        return 0
    else:
        return n + S(n-1)
    
if __name__ == "__main__":
    n = int(input())
    print(S(n))