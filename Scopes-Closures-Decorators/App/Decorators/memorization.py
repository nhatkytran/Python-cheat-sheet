# def fib(n):
#   print('Calculating fib({0})'.format(n))
#   return 1 if n < 3 else fib(n - 1) + fib(n - 2)

print('Memorization with Class')
class Fib:
  def __init__(self):
    self.cache = { 1: 1, 2: 1 }

  def fib(self, n):
    if n not in self.cache:
      print('Calculating fib({0})'.format(n))
      self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
    return self.cache[n]

f = Fib()
# print(f.fib(10))

# //////////
print('Memorization with Closure')
def fib():
  cache = { 1: 1, 2: 1 }

  def inner(n):
    if n not in cache:
      print('Calculating fib({0})'.format(n))
      cache[n] = inner(n - 1) + inner(n - 2)
    return cache[n]

  return inner

f = fib()
# print(f(10))

# //////////
print('Use Decorator')
def fib_decorator(fn):
  from functools import wraps
  cache = { 1: 1, 2: 1 }

  @wraps(fn)
  def inner(n):
    if n not in cache:
      cache[n] = fn(n)
    return cache[n]

  return inner

@fib_decorator
def fib(n):
  print('Calculating fib({0})'.format(n))
  return 1 if n < 3 else fib(n - 1) + fib(n - 2)

# print(fib(10))

# //////////
print('Use Decorator (Slightly changed)')
def fib_decorator(fn):
  from functools import wraps
  cache = dict()

  @wraps(fn)
  def inner(n):
    if n not in cache:
      cache[n] = fn(n)
    return cache[n]

  return inner

@fib_decorator
def fib(n):
  print('Calculating fib({0})'.format(n))
  return 1 if n < 3 else fib(n - 1) + fib(n - 2)

# print(fib(10))

print('Factorial')
@fib_decorator
def fact(n):
  print('Calculating fact({0})'.format(n))
  return 1 if n < 2 else n * fact(n - 1)

# print(fact(10))

# //////////
# Use lru-cache
print('lru cache')
from functools import lru_cache

@lru_cache
def fib(n):
  print('Calculating fib({0})'.format(n))
  return 1 if n < 3 else fib(n - 1) + fib(n - 2)

# print(fib(10))
# print(fib(10))

print('Maxsize')
@lru_cache(8)
def fib(n):
  print('Calculating fib({0})'.format(n))
  return 1 if n < 3 else fib(n - 1) + fib(n - 2)

print(fib(16))
print(fib(8))