class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

p1 = Point(x = 1, y = 2)
# print(p1)

class Point3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

# //////////////////////////////////
from collections import namedtuple

Point2D = namedtuple('Point2D', ['x', 'y'])

pt1 = Point2D(10, 20)
# print(pt1) Point2D(x=10, y=20)

pt3d_1 = Point3D(10, 20, 30)
# print(pt3d_1) <__main__.Point3D object at 0x10bf01b70>

# //////////////////////////////////
Pt2D = namedtuple('Point2D', ('x', 'y'))

pt2 = Pt2D(10, 20)
# print(pt2) Point2D(x=10, y=20)

Pt3D = Point3D

p = Pt3D(10, 20, 30)
# print(p) <__main__.Point3D object at 0x10c412a40>

# //////////////////////////////////
p = Point3D(x=10, y=20, z=30)
# print(p) <__main__.Point3D object at 0x100a672e0>
# print(p.x) 10

# p.x = 100 => It's Ok because the id of p is still the same as before

# //////////////////////////////////
# Check with isinstance
class Point3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

p = Point3D(10, 20, 30)
# print(isinstance(p, tuple)) False

from collections import namedtuple

Point3D = namedtuple('Point3D', ['x', 'y', 'z'])

p = Point3D(x=10, y=20, z=30)
# print(isinstance(p, tuple)) True

# //////////////////////////////////
# Check with "is" and "=="
a = (10, 20)
b = (10, 20)
# print(a is b) True
# print(a == b) True

Point2D = namedtuple('Point2D', ['x', 'y'])

p1 = Point2D(10, 20)
p2 = Point2D(10, 20)
# print(p1 is p2) False
# print(p1 == p2) True

class Point3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

p1 = Point3D(10, 20, 30)
p2 = Point3D(10, 20, 30)
# print(p1 is p2) False
# print(p1 == p2) False

# => Fix Point3D
class Point3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self):
    return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.x == other.x and self.y == other.y
    else:
      return False

p1 = Point3D(10, 20, 30)
p2 = Point3D(10, 20, 30)
# print(p1) Point3D(x=10, y=20, z=30)
# print(p2) Point3D(x=10, y=20, z=30)
# print(p1 is p2) False
# print(p1 == p2) True

# //////////////////////////////////
# Check with max
from collections import namedtuple

Point2D = namedtuple('Poin2D', ['x', 'y'])

p1 = Point2D(10, 20)
# print(max(p1)) 20

class Point3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __repr__(self):
    return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.x == other.x and self.y == other.y
    else:
      return False

p2 = Point3D(10, 20, 30)
# print(max(p2)) 'Point3D' object is not iterable

# => Fix Point3D
class Point3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  # def __repr__(self):
  #   return f'{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})'

  # def __eq__(self, other):
  #   if (isinstance(other, self.__class__)):
  #     return self.x == other.x and self.y == other.y
  #   else:
  #     return False

  def __iter__(self):
    yield self.x
    yield self.y
    yield self.z
# yeild ?????????????????????????????????
p2 = Point3D(10, 20, 30)
# print(max(p2)) 30
# print(max(p2)) 30

# Understand Yield
# def yield_test():
#   yield 1
#   yield 2
#   yield 3

# for i in yield_test():
#   print(i)
# 1 2 3

# for i in yield_test():
#   print(i)
# 1 2 3

# # Hàm in các số chẵn từ mảng arr
# def in_so_chan(arr):
#     for i in arr:
#         if i % 2 == 0:
#             yield i
 
# # Chương trình chính
# mang = [1,4,2,3,5,5,654,66,76,87,8]
# sochan = in_so_chan(mang)
# print(next(sochan))
# print(next(sochan))

# //////////////////////////////////
class Point3D:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

def dot_product_3d(a, b):
  return a.x * b.x + a.y * b.y + a.z * b.z

p1 = Point3D(1, 2, 3)
p2 = Point3D(1, 1, 1)
# print(dot_product_3d(p1, p2)) 6


a = (1, 2)
b = (1, 1)
# print(sum(e[0] * e[1] for e in zip(a, b))) 3

def dot_product(a, b):
  return sum(e[0] * e[1] for e in zip(a, b))

# print(dot_product(a, b)) 3

class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __iter__(self):
    yield self.x
    yield self.y

a = Point2D(1, 2)
b = Point2D(1, 1)
# print(dot_product(a, b)) 3

# //////////////////////////////////
from collections import namedtuple

Vector3D = namedtuple('Vector3D', 'x y z')

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(1, 1, 1)
# print(dot_product(v1, v2)) 6

# //////////////////////////////////
# print(tuple(v1)) (1, 2, 3)
# print(v1) Vector3D(x=1, y=2, z=3)

# //////////////////////////////////
# Person = namedtuple('Person', 'name age _ssn')
# Field names cannot start with an underscore: '_ssn'

Person = namedtuple('Person', 'name age _ssn', rename=True)
# print(Person._fields) ('name', 'age', '_2')

# //////////////////////////////////
Point2D = namedtuple('Point2D', 'x y')

p = Point2D(1, 2)
# print(p._asdict()) {'x': 1, 'y': 2}