a = 1, 2, 3
b = (1, 2, 3)

# print(a) (1, 2, 3)
# print(b) (1, 2, 3)
# print(type(a)) <class 'tuple'>
# print(type(b)) <class 'tuple'>

# In some case, have to specify the round parentheses
def print_tuple(t):
  for e in t:
    print(e)

# print_tuple(1, 2, 3) print_tuple() takes 1 positional argument but 3 were given
# print_tuple((1, 2, 3))
# 1
# 2
# 3

a = 1, 2, 3, 4, 5

# print(a[0]) 1
# print(a[0:2]) (1, 2)

a = 1, 2, 3
x, y, z = a

# print(x, y, z) 1 2 3

a = 1, 2, 3, 4, 5
x, *_, y, z = a

# print(x, y, z) 1 4 5
# print(_) [2, 3]

a = 1, 2, 3
# a[0] = 0 'tuple' object does not support item assignment

class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __repr__(self):
    return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

# pt = Point2D(10, 20)
# print(pt)
# print(id(pt))
# pt.x = 100
# print(pt)
# print(id(pt))

# Point2D(x=10, y=20)
# 4333567952
# Point2D(x=100, y=20)
# 4333567952

pt = Point2D(10, 20), Point2D(30, 40)

# print(id(pt[0]))
# pt[0].x = 100
# print(id(pt[0]))
# 4378165200
# 4378165200

s = 'python'
# print(id(s))
s = 'python' + ' rocks'
# print(id(s))
# 4531533680
# 4531791024

a = 1, 2, 3
# print(id(a))
a += 4, 5
# print(id(a))
# 4445525632
# 4445809904

# print(type(8_700)) <class 'int'>

# Heterogeneous and Homogeneous //////////
london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000
# Heterogeneous

cities = [london, new_york, beijing]
# Homogeneous

# List comprehension
# print([city[2] for city in cities]) [8780000, 8500000, 21000000]
# print(sum([city[2] for city in cities])) 38280000
# print(sum(city[2] for city in cities)) 38280000

# for a, b ,c in cities:
#   print(a, b, c)
# London UK 8780000
# New York USA 8500000
# Beijing China 21000000

# for item in enumerate(cities):
#   print(item)
# (0, ('London', 'UK', 8780000))
# (1, ('New York', 'USA', 8500000))
# (2, ('Beijing', 'China', 21000000))

from random import uniform
from math import sqrt

def random_shot(radius):
  random_x = uniform(-radius, radius)
  random_y = uniform(-radius, radius)
  
  if (sqrt(random_x ** 2 + random_y **2) <= radius):
    is_in_circle = True
  else:
    is_in_circle = False

  return random_x, random_y, is_in_circle

num_attemps = 1000000
count_inside = 0

for i in range(num_attemps):
  *_, is_in_circle = random_shot(1)
  
  if (is_in_circle):
    count_inside += 1

Pi = 4 * count_inside / num_attemps
print(Pi)