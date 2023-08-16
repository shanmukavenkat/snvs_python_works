num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
# Write your code here
n = int(input())
new_list = []
for tuple_a in num_list:
    new_tuple = tuple_a
    if n in tuple_a:
        n_index = tuple_a.index(n)
        new_tuple = tuple_a[:n_index]+tuple_a[n_index+1:]
    new_list.append(new_tuple)
print(new_list)