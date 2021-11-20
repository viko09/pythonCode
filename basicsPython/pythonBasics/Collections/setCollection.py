# Set Collection: Don't keep an order and neither allow modify the elements
planets = {'Mars', 'Jupyter', 'Venus'}
print(planets)

print(len(planets))
# Review if an element exist
print('Mars' in planets)  # True
print('Earth' in planets)  # False
# Add elements
planets.add('Earth')
print(planets)
# We can't duplicate elements on sets
planets.add('Earth')
print(planets)
# Remove elements
planets.remove('Venus')
print(planets)
# Discard elements, if the element is not on the set, we don't get an error
planets.discard('Jupyter')
print(planets)
