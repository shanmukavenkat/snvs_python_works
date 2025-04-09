a = input().split(",")
b = input().split(",")
students_dict = {}
for i in range(len(a)):
    key = a[i]
    value = b[i]
    students_dict[key] = value
dict_a = students_dict.items()
sorted_dict = sorted(dict_a)
for item in sorted_dict:
    print(*item)


