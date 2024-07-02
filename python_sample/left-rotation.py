def rotLeft(a, d):
    return a[d:] + a[:d],a[-d:] + a[:-d]
# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shift = 2
shifted_array = rotLeft(array, shift)

# Print the shifted array
for element in shifted_array:
    print(element, end=" ")
