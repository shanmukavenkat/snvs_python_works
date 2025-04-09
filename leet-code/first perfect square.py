m = int(input())
n = int(input())

perfect_square = 0
for i in range(m,n+1):
    if i == int(i**0.5)**2:
        perfect_square = i
        break
if perfect_square > 0:
    print(perfect_square)
else:
    print("No Perfect Square")
