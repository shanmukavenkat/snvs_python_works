for i in  range(5):
    for j in range(6):
        if(j == 0 or j == 5) and  0<i<4:
            print("*",end ="")
        elif (i==0 or i == 4) and 0<j<5:
            print("*",end="")
        else:
            print(end=" ")
    print()