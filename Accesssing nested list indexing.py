
list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
n = int(input())
list_b = []

for i in range(n):
    index = input().split()
    tuple_index = int(index[0])
    value_index = int(index[1])
    value = list_a[tuple_index][value_index]
    list_b.append(value)
print(list_b)
