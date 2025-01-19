if __name__ =='__main__':
    tc = int(input())
    for _ in range(tc):
        s = input().split()
        for i in range(len(s)):
            if s[1] == '+':
                print(int(s[0]) + int(s[2]))
            elif s[1] == '*':
                print(int(s[0]) * int(s[2]))