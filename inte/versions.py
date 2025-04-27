print("major.minor.micro")
print("3.12.2")
print("in some minor version there are some breaking changes")
print("In micro version there are some of the bug fixes these are the changes")
a = 5
if a == 3:
    print("The Statements true")
else:
    print("the Statements false")

b = 2
b = b+2
print(b)


print(2/3)
# it is float division 1.5
print(2%3)
# it is modulus division 1
print(2//3)
# it is floor division 0


print("====================================================")

try:
    result = int("abc")
except:
    print("You are trying to divide by zero")

print("====================================================")

#try:
     #code
#except:
    #code
#else:
    #code if no exception errors
#finally:
    #code always executed regardless of exception
print("====================================================")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("exception")
else:
    print('Hello world')
finally:
    print("This block always executes regardless of exceptions.")

