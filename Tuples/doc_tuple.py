from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')

# print(Point2D.__doc__) Point2D(x, y)
# print(Point2D.x.__doc__) Alias for field number 0
# print(Point2D.y.__doc__) Alias for field number 1

# print(help(Point2D))

# /////////////////////////////////////////////////////
# Prototype approach
from collections import namedtuple

Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)
v = vector_zero._replace(x1 = 1, y1 = 2, x2 = 3, y2 = 4)

# print(v)
# Vector2D(x1=1, y1=2, x2=3, y2=4, origin_x=0, origin_y=0)

# /////////////////////////////////////////////////////
# __defaults__
def func(a, b=1, c=2):
  print(a, b, c)

# func(1) 1 1 2

# print(func.__defaults__) (1, 2)

func.__defaults__ = 10, 20, 30
# func() 10 20 30

from collections import namedtuple

Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
Vector2D.__new__.__defaults__ = 0, 0
v = Vector2D(1, 2, 3, 4)
# print(v) Vector2D(x1=1, y1=2, x2=3, y2=4, origin_x=0, origin_y=0)
