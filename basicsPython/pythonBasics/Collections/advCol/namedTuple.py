# Created by. Viko Luna
# Named Tuple: Allow creating tuples and allow assing meaningful names
# to the positions of the items. Tuple + Class == NamedTuple

from collections import namedtuple
point_2d = namedtuple('point_2D', ['x', 'y'])
new_point = point_2d(50, 100)
print(new_point)

print(isinstance(new_point, point_2d))
print(isinstance(new_point, tuple))

# Unpacking Tuple
x, y = new_point
print(f'{x}, {y}')

# Index Numbers
x = new_point[0]
y = new_point[1]
print(f'({x}, {y})')

# Iterate over new point
for item in new_point:
    print(item)

