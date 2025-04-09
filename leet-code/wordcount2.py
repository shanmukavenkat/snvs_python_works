word = input().split()
length = set(word)
for i in sorted(length):
    msg ="{i}: {count}"
    print(msg.format(i=i,count=word.count(i)))
