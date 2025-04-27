print("it has a global scope")

#def function_name(parameter):
#    # function body
#    # code to be executed
#    return value

def greet(name):
    return f"Hello, {name}!"

name = input("Enter your name: ")
print(greet(name))  # Output: Hello, Alice!
## it is user defined function

def add_number(a,b):
    return a+b
result = add_number(5, 10)
print(result)  # Output: 15

print("<><><><><><><><><><><>><<><><><><>><><><><><<><>><><><><><<><><<<")

print("""
When people say arbitrary arguments in Python, they mean:

"The function can take any number of inputs — not fixed — as many as you want."

And that is exactly why we use *args and **kwargs!

*args → for any number of positional arguments (like values without names)

**kwargs → for any number of keyword arguments (like name=value pairs)
""")

print("<><><><><><><><><><><>><<><><><><>><><><><><<><>><><><><><<><><<<")

def print_name(*names):
    for i in names:
        print(i)


print_name("Alice", "Bob", "Charlie")
print("<><><><><><><><><><><>><<><><><><>><><><><><<><>><><><><><<><><<<")

print("""
the print(),
len(), and range(),type(),min(),max(),sum(),int(),float(),str(),list(),dict(),set(),tuple(),sorted(),reversed(),enumerate()
,zip() functions are built-in functions in Python.
""")

print("-------------------------------------------------------------------")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

print("""
factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * (1 * factorial(0)))))
= 5 * (4 * (3 * (2 * (1 * 1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120
  it is also known as the recursion function""")

print("-------------------------------------------------------------------")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5