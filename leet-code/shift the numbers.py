a = input()
string = ""
string2 = ""
k = 57
for i in a:
    if ord(i) <= k:
        string += i
    elif ord(i) > k:
         string2 += i
print(string2+string)

