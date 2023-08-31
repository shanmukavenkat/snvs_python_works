a = input()
b = input()
for i in b:
    if len(a) != len(b):
        result = "No Match"
    elif a[0] == i:
        result = b.index(i)
        break
    else:
        result = "No Match"
print(result)