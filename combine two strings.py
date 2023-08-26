def convert_string_to_int(str_num_list):
    int_list =[]
    for str_num in str_num_list:
        num = int(str_num)
        int_list.append(num)
    return int_list
#convert keys and values to dictionary
def convert_to_key_value_pairs(keys_list,values_list):
    dict_a ={}
    number_of_keys = len(keys_list)
    for i in range(number_of_keys):
        key = keys_list[i]
        value = values_list[i]
        dict_a[key] = value
    return dict_a

dict_a_keys = input().split()
dict_a_values = input().split()
dict_b_keys = input().split()
dict_b_values = input().split()

dict_a_values = convert_string_to_int(dict_a_values)
dict_b_values = convert_string_to_int(dict_b_values)

student_details_1 = convert_to_key_value_pairs(dict_a_keys, dict_a_values)
student_details_2 = convert_to_key_value_pairs(dict_b_keys, dict_b_values)

student_details_1.update(student_details_2)
student_details = student_details_1.items()
student_details = sorted(student_details)
print(student_details)