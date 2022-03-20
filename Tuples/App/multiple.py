from random import randint, random
from collections import namedtuple

def random_color():
  red = randint(0, 255)
  green = randint(0, 255)
  blue = randint(0, 255)
  alpha = round(random(), 1)
  return red, green, blue, alpha

color = random_color()
# print(color) (19, 253, 102, 0.8)
# print(color.red) AttributeError: 'tuple' object has no attribute 'red'

Color = namedtuple('Color', 'red green blue alpha')

def random_color():
  red = randint(0, 255)
  green = randint(0, 255)
  blue = randint(0, 255)
  alpha = round(random(), 1)
  return Color(red, green, blue, alpha)

color = random_color()
# print(color) Color(red=78, green=252, blue=90, alpha=0.4)
# print(color.red) 78