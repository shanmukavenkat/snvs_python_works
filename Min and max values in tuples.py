n = int(input())
num_list = []
zero_index = []
first_index = []
for i in range(n):
    values_list = input().split()
    first_value = int(values_list[0])
    zero_index.append(first_value)
    second_value = int(values_list[1])
    first_index.append(second_value)
zero_index_min_max_tuple = (max(zero_index),min(zero_index))
first_index_min_max_tuple = (max(first_index),min(first_index))
print(zero_index_min_max_tuple)
print(first_index_min_max_tuple)

