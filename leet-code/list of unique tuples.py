def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list

n = int(input())
num_list = []
for i in range(n):
    values_list = input().split()
    values_list = convert_string_to_int(values_list)
    values_set = set(values_list)
    is_equal = len(values_list) == len(values_set)
    if is_equal:
        num_list.append(values_list)
print(num_list)