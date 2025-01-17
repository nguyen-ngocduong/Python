#Xâu đối xứng
#Ký tự xuất hiện nhiều nhất trong xâu
if __name__ == '__main__':
    s = input()
    t = s[::-1]
    if s == t:
        print("YES")
    else:
        print("NO")