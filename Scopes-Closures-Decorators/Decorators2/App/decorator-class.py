def my_dec(a, b):
  def dec(fn):
    def inner(*args, **kwargs):
      print('Decorated function called: a = {0}, b = {1}'.format(a, b))
      return fn(*args, **kwargs)
    return inner
  return dec

@my_dec(10, 20)
def my_func(s):
  print('Hello {0}'.format(s))

# my_func('World')
# Decorated function called: a = 10, b = 20
# Hello World

# Class is callable
class MyClass:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __call__(self, c):
    print('Called a = {0}, b = {1}, c = {2}'.format(self.a, self.b, c))

obj = MyClass(10, 20)

# obj(30)
# Called a = 10, b = 20, c = 30

# Class and decorator
class MyClass:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __call__(self, fn):
    print('Called a = {0}, b = {1}'.format(self.a, self.b))
    def inner(*args, **kwargs):
      print('Decorated function called: a = {0}, b = {1}'.format(self.a, self.b))
      return fn(*args, **kwargs)
    return inner

# @MyClass(10, 20)
# def my_func(s):
#   print('Hello {0}'.format(s))

# my_func('World')
# Called a = 10, b = 20
# Decorated function called: a = 10, b = 20
# Hello World

# obj = MyClass(10, 20)
# def my_func(s):
#   print('Hello {0}'.format(s))
# my_func = obj(my_func)
# my_func('World')
# Called a = 10, b = 20
# Decorated function called: a = 10, b = 20
# Hello World

# obj = MyClass(10, 20)
# @obj
# def my_func(s):
#   print('Hello {0}'.format(s))

# my_func('World')
# Called a = 10, b = 20
# Decorated function called: a = 10, b = 20
# Hello World