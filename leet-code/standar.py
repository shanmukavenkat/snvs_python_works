import math
print(math.factorial(5))
print(math.pi )
import random
random_number = random.randint(1,20)
print(random_number)
print("--------------------------------")
k = random.choice([1,2,3,4,5,6,7,8,9,10])
print(k)
def square(n):
    return n*n
num = [1,2,3,4,5,]
result = map(square, num)
print(list(result))
print("--------------------------------")
def convert_str_to_int(m):
    k = []
    for i in m:
        s = int(i)
        k.append(s)
    return k
num = ["1","2","3","4","5"]
result = convert_str_to_int(num)
print(result)
from functools import reduce
print("-----------------------------------------------")
def sum_of_num(num1,num2):
    return num1+num2
num = [1,2,3,4,5]
result = reduce(sum_of_num,num)
print(result)