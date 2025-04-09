given_input = list(map(int,input().split()))

given_list = sorted(set(given_input))

max_num = max(given_list)
for i in range(1,(max_num)+2):
    if i not in given_list:
        print(i)
        break