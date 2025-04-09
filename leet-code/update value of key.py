students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

k = input().split()
key, value = k[0],k[1]
students_dict[key]= value
print(students_dict)
