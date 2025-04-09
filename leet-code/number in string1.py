from statistics import mean


a = input()
num = ""
k = num
for i in a:
    if i.isdigit():
        num += i

sum_of = 0
for i in num:
    sum_of += int(i)
print(sum_of)

avg = sum_of/ len(num)
print(avg)
