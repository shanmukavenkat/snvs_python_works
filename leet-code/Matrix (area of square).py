def get_area_square(matrix,row,col):
    max_area_square = 0
    for i in range(row):
        for j in range(col):
            if (matrix[i][j] == "X"):
                max_sub_matrix_area = get_max_sub_matrix(matrix,row,col,i,j)
                max_area_square = max(max_area_square,max_sub_matrix_area)
    return max_area_square



def get_max_sub_matrix(matrix,row,col,i,j):
    max_sub_matrix_area = 0
    for k in range(row-i):
        for l in range(col-j):
            if (k==l):
                is_zero_contains = check_if_zero_contains(matrix,k,l,i,j)
                if not is_zero_contains:
                    max_sub_matrix_area = max(max_sub_matrix_area,(k+1)*(l+1))

    return max_sub_matrix_area

def check_if_zero_contains(matrix,k,l,i,j):
    for m in range(0,k+1):
        for n in range(0,l+1):
            if (matrix[m+i][n+j]=="O"):
                return True
    return False




row, col = [int(i) for i in input().split()]
#print(row,col)
matrix = []

for i in range(row):
    matrix.append(input().split())

max_area_square = get_area_square(matrix,row,col)
print(max_area_square)