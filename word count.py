word = input().split()
dict_a = dict()
for  each_word in word:
    if each_word not in dict_a:
        dict_a[each_word] = 1
    else:
        dict_a[each_word] += 1
for key,value in dict_a.items():
    pair = "{key}: {value}"
    print(pair.format(key=key,value=value))
