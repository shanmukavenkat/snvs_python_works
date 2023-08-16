def get_sum_of_matrix(nested_list):
  total = 0
  for each_list in nested_list:
    total += sum(each_list)
  return total

def convert_string_to_int(list_a):
  new_list = []
  for item in list_a:
    num = int(item)
    new_list.append(num)
  return new_list

m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
  list_a = input().split()
  list_a = convert_string_to_int(list_a)
  num_list.append(list_a)

print(max(max(num_list)))
print(min(min(num_list)))
total = get_sum_of_matrix(num_list)
print(total)