number = input().split()
for i in number:
    if i == "+":
        print(int(number[0]) + int(number[2]))
    elif i == "-":
        print(int(number[0]) - int(number[2]))
    elif i == "*":
        print(int(number[0]) * int(number[2]))
    elif i == "/":
        print(int(number[0]) // int(number[2]))
    elif i == "%":
        print(int(number[0]) % int(number[2]))
    elif i == "**":
        print(int(number[0]) ** int(number[2]))
    else:
        continue