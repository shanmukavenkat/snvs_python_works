s = input()
digits = ""
for i in s:
    if i.isdigit() or i == " ":
        digits += i
    else:
        digits += " "
digits = digits.split()

sum_of = 0
for i in range(len(digits)):
    sum_of += int(digits[i])
print(sum_of)

avg = sum_of / len(digits)
print(avg)
