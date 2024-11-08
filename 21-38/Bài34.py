a = int(input("Nhập chiều ngang a: "))
b = int(input("Nhập chiều dài b: "))
for i in range (a):
    for j in range (b) :
        if j == 0 or j == a  :
            print ("*", end = " ")
        elif i == 0 or i == a-1:
            print("*", end = " ")
        else :
            print("~", end =" ")
    print()            
