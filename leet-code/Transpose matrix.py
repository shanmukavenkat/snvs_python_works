def get_transpose_of_matrix(matrix, m, n):
    transpose_matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix[j][i])
        transpose_matrix.append(row)
    return transpose_matrix

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
transpose_matrix = get_transpose_of_matrix(num_list,m,n)

for row in transpose_matrix:
    print(row)
