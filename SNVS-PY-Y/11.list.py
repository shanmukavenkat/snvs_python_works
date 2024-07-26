import math
x = [1,2,3,4,5,6]
y = 8

squares = [i**2 for i in x]
print(str(squares))

new = math.prod(x)
new1 = math.fsum(x)
new2 = math.sqrt(y)
print("sum",new1)
print("sqrt",new2)
print(new)
