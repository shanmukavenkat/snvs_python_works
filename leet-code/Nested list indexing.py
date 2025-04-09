num_list = [(2, 4, 6, 8), (5, 15, 25, 35), (7, 14, 21)]

n = int(input())
for tuple_a in num_list:
    is_contained = n in tuple_a
    if is_contained:
        tuple_index = num_list.index(tuple_a)
       # print(tuple_index)
        n_index = tuple_a.index(n)
       # print(n_index)
        print(str(tuple_index)+" "+str(n_index))
        break