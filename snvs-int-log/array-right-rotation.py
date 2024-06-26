def left_rotation(a,b):
    return a[b:] + a[:b]


a = list(map(int,input().split()))
b = int(input())

letNumbers = left_rotation(a,b)
print(letNumbers)
