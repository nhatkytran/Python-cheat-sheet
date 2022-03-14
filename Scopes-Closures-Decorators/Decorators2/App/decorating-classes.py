from fractions import Fraction

f = Fraction(2, 3)

# print(f.numerator) 2
# print(f.denominator) 3

Fraction.hi = 2

# print(f.hi) 2

Fraction.speak = lambda self, message: 'Fraction says: {0}'.format(message)

# => Monkey patching

# print(f.speak('Live a positive life'))
# Fraction says: Live a positive life

f1 = Fraction(2, 3)
f2 = Fraction(64, 8)

# print(f1) 2/3
# print(f2) 8

Fraction.is_integral = lambda self: self.denominator == 1

# print(f1.is_integral()) False
# print(f2.is_integral()) True

def dec_speak(cls):
  cls.speak = lambda self, message: '{0} says: {1}'.format(self.__class__.__name__, message)
  return cls

Fraction = dec_speak(Fraction)

f = Fraction(2, 3)

# print(f.speak('Hi'))
# Fraction says: Hi

class Person:
  pass

Person = dec_speak(Person)
p = Person()

# print(p.speak('Hello World'))
# Person says: Hello World

class Num:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def check_vars(self):
    print(self)
    print(vars(self))

number = Num(10, 20)

# number.check_vars()
# <__main__.Num object at 0x10339ab30>
# {'a': 10, 'b': 20}

# ////////////////////////////////////////
from datetime import datetime, timezone

def info(self):
  results = []
  results.append('time: {0}'.format(datetime.now(timezone.utc)))
  results.append('Class: {0}'.format(self.__class__.__name__))
  results.append('id: {0}'.format(hex(id(self))))
  for k, v in vars(self).items():
    results.append('{0}: {1}'.format(k, v))
  return results
  
def debug_info(cls):
  cls.debug = info
  return cls

@debug_info
class Person:
  def __init__(self, name, birth_year):
    self.name = name
    self.birth_year = birth_year

  def say_hi(self):
    return 'Hello there!'

p = Person('Frlix', 2002)

# print(p.debug())
# ['time: 2022-02-28 00:37:25.350696+00:00', 'Class: Person', 'id: 0x1102a3970', 'name: Frlix', 'birth_year: 2002']

# ////////////////////////////////////////
from datetime import datetime, timezone

def info(self):
  results = []
  results.append('time: {0}'.format(datetime.now(timezone.utc)))
  results.append('Class: {0}'.format(self.__class__.__name__))
  results.append('id: {0}'.format(hex(id(self))))
  for k, v in vars(self).items():
    results.append('{0}: {1}'.format(k, v))
  return results
  
def debug_info(cls):
  cls.debug = info
  return cls

@debug_info
class Automobile:
  def __init__(self, make, model, year, top_speed):
    self.make = make
    self.model = model
    self.year = year
    self.top_speed = top_speed
    self._speed = 0

  @property
  def speed(self):
    return self._speed

  @speed.setter
  def speed(self, new_speed):
    if new_speed > self.top_speed:
      raise ValueError('Speed cannot exceed top_speed.')
    else:
      self._speed = new_speed

favorite = Automobile('Ford', 'Model T', 1908, 45)

# print(favorite.debug())
# ['time: 2022-03-01 00:04:00.615586+00:00', 'Class: Automobile', 'id: 0x105363fd0', 'make: Ford', 'model: Model T', 'year: 1908', 'top_speed: 45', '_speed: 0']

# favorite.speed = 100
# print(favorite.debug())
# ValueError: Speed cannot exceed top_speed.

# favorite.speed = 40
# print(favorite.debug())
# ['time: 2022-03-01 00:06:53.674032+00:00', 'Class: Automobile', 'id: 0x10b8cbfd0', 'make: Ford', 'model: Model T', 'year: 1908', 'top_speed: 45', '_speed: 40']

from math import sqrt

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __abs__(self):
    return sqrt(self.x ** 2 + self.y ** 2)

  def __repr__(self):
    return 'Point({0}, {1})'.format(self.x, self.y)

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

# print(repr(p1)) Point(2, 3)
# print(abs(p1)) 3.605551275463989
# print(p1 is p2) False

# ////////////////////////////////////////
# print(p1 == p2) False => Fix equality for class
# print(isinstance(p1, Point)) True

from math import sqrt

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __abs__(self):
    return sqrt(self.x ** 2 + self.y ** 2)

  def __repr__(self):
    return 'Point({0}, {1})'.format(self.x, self.y)

  def __eq__(self, other):
    if isinstance(other, Point):
      return self.x == other.x and self.y == other.y
    else:
      return False

  def __lt__(self, other):
    if isinstance(other, Point):
      return abs(self) < abs(other)
    else:
      return NotImplemented

  # def __le__(self, other):
  #   pass

  # def __gt__(self, other):
  #   pass

  # def __ge__(self, other):
  #   pass

  # def __ne__(self, ohter):
  #   pass


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)

# print(p1 is p2) False
# print(p1 == p2) True

# print(p1 < p2) False
# print(p1 > p3) True

# class Test:
#   pass
# p4 = Test()

# print(p1 < p4)
# TypeError: '<' not supported between instances of 'Point' and 'Test'

# ////////////////////////////////////////
# Not truly Python code behinds the scene but to get the point
from math import sqrt

def complete_ordering(cls):
  if '__eq__' in dir(cls) and '__lt__' in dir(cls):
    cls.__le__ = lambda self, other: self < other or self == other
    cls.__gt__ = lambda self, other: not (self < other) and not (self == other)
    cls.__ge__ = lambda self, other: not (self < other)
  return cls

@complete_ordering
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __abs__(self):
    return sqrt(self.x ** 2 + self.y ** 2)

  def __repr__(self):
    return 'Point({0}, {1})'.format(self.x, self.y)

  def __eq__(self, other):
    if isinstance(other, Point):
      return self.x == other.x and self.y == other.y
    else:
      return False

  def __lt__(self, other):
    if isinstance(other, Point):
      return abs(self) < abs(other)
    else:
      return NotImplemented

p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)

# print(p1 <= p4) True
# print(p4 >= p2) True
# print(p1 != p2) False

# ////////////////////////////////////////
from functools import total_ordering

@total_ordering
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __abs__(self):
    return sqrt(self.x ** 2 + self.y ** 2)

  def __repr__(self):
    return 'Point({0}, {1})'.format(self.x, self.y)

  def __eq__(self, other):
    if isinstance(other, Point):
      return self.x == other.x and self.y == other.y
    else:
      return False

  def __lt__(self, other):
    if isinstance(other, Point):
      return abs(self) < abs(other)
    else:
      return NotImplemented

p1, p2, p3, p4 = Point(2, 3), Point(2, 3), Point(0, 0), Point(100, 200)

# print(p1 <= p2) True
# print(p1 >= p4) False
# print(p4 > p1) True

class Person:
  def __init__(self, first_name):
    self.first_name = first_name

me = Person('Frlix')

# print(Person.__name__) Person
# print(me.__class__.__name__) Person
