def right_rotation(a,d):
    return a[-d:] + a[:-d]


a = list(map(int,input().split()))
b = int(input())

letNumbers = right_rotation(a,b)
print(letNumbers)
