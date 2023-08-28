a = input().split()
b = int(input())
result = ""
for i in a:
    if len(i) == b:
        continue
    result += i + " "
print(result)
