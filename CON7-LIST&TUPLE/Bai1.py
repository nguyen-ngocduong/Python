#tính tổng chẵn lẻ
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    chan, le, tongchan, tongle = 0,0,0,0
    for x in a:
        if x % 2 == 0:
            chan+=1
            tongchan += x
        else:
            le += 1
            tongle += x
    print(chan, le, tongchan, tongle, sep = '\n')