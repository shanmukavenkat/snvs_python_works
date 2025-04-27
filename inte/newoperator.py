## ternary operators

age = 20
message = "adult" if age>=18 else "teenager"
print(message)  # Output: adult
new = 12
## match variable
match new:
    case  23:
        print("value1")
    case  12:
        print("value2 answer 12")
    case _:
        ## this is a default case
        print("default")

## match statement
i = 5
while i<= 5:
    print(i)
    i += 1

# Example usage of the id() function
my_list = [1, 2, 3]

# Get the identity of the list
list_id = id(my_list)

# Print the result
print("Identity of my_list:", list_id)


