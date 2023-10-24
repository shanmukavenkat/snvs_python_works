sentence = input().split()
#convert to separated string
sentence.sort()
#oreder of sentences through sort
store = set()
for i in range(len(sentence) ): #here length of sentence to iterate
    for j in range(i+1,len(sentence)): # here add the i+1 (add with call to in other words)
        for k in range(j+1, len(sentence)): # here add the j+1 (add with call to in other words)
            s = sentence[i] + " " + sentence[j] + " " + sentence[k]
            store.add(s)
#print(store)
set_convert_list = list(store)
#print(set_convert_list)
set_convert_list.sort()
#print(set_convert_list)
for i in set_convert_list:
    print(i)


