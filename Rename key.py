fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Rename the key "mangoes" to "grapes"
a = input()
b = input()
fruit_items = list(fruits.items())
fruit_items_copy = fruit_items.copy()
fruits_count = len(fruits)

for i in range(fruits_count):
    if fruit_items[i][0] == a:
        updated_tuple = (b,fruit_items[i][1])
        fruit_items_copy[i] = updated_tuple
print(fruit_items_copy)


