def get_con_sum_list(int_list):
    con_sum_list = []
    for i in range(len(int_list)-1):
        con_sum_ = int_list[i]+ int_list[i+1]
        con_sum_list.append(con_sum_)
    return con_sum_list

def print_sum_triangle(int_list):
    while len(int_list )> 1:
        con_sum = get_con_sum_list(int_list)
        print(con_sum)
        int_list = con_sum
def convert_str_to_list(str_num_list):
    int_list = []
    for item in str_num_list:
        num = int(item)
        int_list.append(num)
    return int_list


str_num_list = input().split(",")
int_list = convert_str_to_list(str_num_list)
print(int_list)
print_sum_triangle(int_list)