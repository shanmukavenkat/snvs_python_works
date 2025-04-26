a = int(input())
total = 0
for i in range(1,a+1):
    p = list(map(int, input().split(',')))
    print(p)
    total = total + sum(p)
print(float(total)/a)
