m,n = map(int,input().split())
new_list =[]

for i in range(m):
    list_a = list(map(int,input().split()))
    new_list.append(list_a)

stop_index = m+n+1
for i in range(stop_index):
    for j in range(i+1):
        if j < m and i-j < n:
            print(new_list[j][i-j],end="")
    print()


