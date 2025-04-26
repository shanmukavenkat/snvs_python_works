a = int(input())
count = 0
while a != 0:
    lastdigit = a%10
    a = a//10
    count = count+1
    print(lastdigit)
print("the numbers:",count)