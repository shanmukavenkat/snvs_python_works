prefix = input()
suffix = input()
result = ""
for i in range(len(prefix)):
    if suffix.startswith(prefix[i:]):
        result = prefix[i:]
        break
if result == "":
    print("No overlapping")
print(result)