n = int(input())
m = input().split()
product = 1
for i in m:
    product = product * int(i)
print(product % (10**9+7))