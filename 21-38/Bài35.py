h = int(input("Nhập chiều cao h: "))
for i in range(h) :
    for j in range (h) :
        if j == 0 or j == h-1 or i==j:
            print ("*", end = " ")
        else :
            print(" ", end = " ")
    print()        
