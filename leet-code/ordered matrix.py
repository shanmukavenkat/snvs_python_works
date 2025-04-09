m,n = list(map(int,input().split()))
matrix = []
for i in range(m):
    matrix += list(map(int,input().split()))

sorted_list = sorted(matrix)
counter = 0
for i in range(m):
    row = ""
    for j in range(n):
        row += str(sorted_list[counter])+ " "
        counter += 1
    print(row)

