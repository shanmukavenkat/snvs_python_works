def read_matrix(n):
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def single_rotate_clockwise(matrix):
    n = len(matrix[0])
    temp_matrix = []
    for i in range(n):
        column = []
        for row in matrix:
            column.append(row[i])
        temp_matrix.append(column[::-1])
    return temp_matrix

def rotate_matrix(matrix, degrees):
    n = len(matrix[0])
    rotations = (degrees // 90) % 4
    for r in range(rotations):
        matrix = single_rotate_clockwise(matrix)
    return matrix

def main():
    n = int(input())
    matrix = read_matrix(n)
    original_matrix = matrix
    total_rotation = 0
    while True:
        line = input().split()
        if line[0] == "-1":
            break
        elif line[0] == "R":
            rotation = int(line[1])
            total_rotation += rotation
            matrix = rotate_matrix(matrix, rotation)
        elif line[0] == "U":
            ri, ci, value = int(line[1]), int(line[2]), int(line[3])
            original_matrix[ri][ci] = int(value)
            matrix = rotate_matrix(original_matrix, total_rotation)
        elif line[0] == "Q":
            ri, ci = int(line[1]), int(line[2])
            print(matrix[ri][ci])

main()