t = int(input())
for i in range(t):
    a = int(input())

    if (a%100==0 and a%400 == 0):
        print("leap year")
    elif(a%100!=0 and a%4 == 0):
        print("leap year")
    else:
        print("not")

