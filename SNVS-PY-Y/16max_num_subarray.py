n = input().split(",")
list_n = [int(x) for (x) in n]

new_num = list_n

sum = []
for i in range(1,len(new_num)):
    var = new_num[i] * new_num[i-1]
    sum.append(var)
print((sum))
print(max(sum))
