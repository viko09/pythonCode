# Dictionaries saves data organized by:
# Key and Value: dict(key, value)

dictionary = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(dictionary)

# Len of dictionary
print(len(dictionary))

# Accessing into an element
print(dictionary['IDE'])
print(dictionary.get('OOP'))

# Modify elements
dictionary['IDEV'] = 'Integrated Development Environment of Viko'
print(dictionary)

# Check elements
for place in dictionary:
    print(place)

for place, value in dictionary.items():
    print(place, value)

for place in dictionary.keys():
    print(place)

for value in dictionary.values():
    print(value)

# Check existence of elements
print('IDe' in dictionary)

# Add elements into a dictionary, we can not add the same key twice
dictionary['PK'] = 'Primary Key'
print(dictionary)

# Remove elements
dictionary.pop('DBMS')
print(dictionary)

# Clear all elements
dictionary.clear()
print(dictionary)

# Remove Dictionary
del dictionary
