# def add(a, b):
#   return a + b

def outer(fn):
  def inner(*args, **kwargs):
    return fn(*args, **kwargs)

  return inner

# add = outer(add)
# print(add(1, 2)) # 3
# /////////////////////////////////
# Decorators with @symbol
@outer
def add(a, b):
  return a + b

print(add(1, 2)) # 3
print(add.__name__) #inner
print(add.__doc__) # None

import inspect
print(inspect.signature(add)) # *args, **kwargs

from functools import wraps

def outer(fn):
  @wraps(fn)
  def inner(*args, **kwargs):
    return fn(*args, **kwargs)

  return inner

@outer
def add(a, b):
  return a + b

print(inspect.signature(add)) # (a, b)