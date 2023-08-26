students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

k = int(input())
for i in range(k):
    key,value = input().split()
    students_dict[key] = value
print(students_dict)