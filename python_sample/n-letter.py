num = int(input())
for i in range(1,num):
    space = " "
    n_space = space*i
    print("*"+ n_space + "*" + space*(num-i)+"*")

