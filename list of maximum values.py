num = int(input())
lists_1 = []


def nested_list(list_1):
    list_2 = []
    for item in list_1:
        num_2 = int(item)
        list_2.append(num_2)
    return max(list_2)

for i in range(num):
    list_1 = input().split()
    list1 = nested_list(list_1)
    lists_1.append(list1)
print(lists_1)

