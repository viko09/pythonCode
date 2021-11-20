# Define a tuple
fruits = ('Orange', 'Banana', 'Grape', 'Watermelon', 'Lemon')
print(fruits)

# Number of elements
print(len(fruits))

# Access into an element
print(fruits[0])

# Access to the last element
print(fruits[-1])

# Print a range
print(fruits[0:2])

# Specify a comma if we have just 1 element
justone = ('Cuba', )
print(justone)

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    print(fruit, end=' ')

# Modify an element, convert to a list, after, change the element and finally, convert to a tuple
fruitsList = list(fruits)
fruitsList[0] = 'Apple'
fruits = tuple(fruitsList)
print('\n', fruits)

# Delete the tuple
del fruits
print('Successfully Deleted')
