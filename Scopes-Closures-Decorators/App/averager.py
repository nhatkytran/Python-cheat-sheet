# Use class
print('Use class')
class Averager:
  def __init__(self):
    self.numbers = []

  def add(self, number):
    self.numbers.append(number)
    total = sum(self.numbers)
    count = len(self.numbers)
    return total / count

average = Averager()
print(average.add(10)) # 10
print(average.add(20)) # 15

print('Use class - rewrite')
class Avenger:
  def __init__(self):
    self.total = 0
    self.count = 0
  
  def __add__(self, number):
    self.total += number
    self.count += 1
    return self.total / self.count

average = Averager()
print(average.add(10)) # 10
print(average.add(20)) # 15
# Use closure
print('Use closure')
def averager():
  numbers = []

  def add(number):
    numbers.append(number)
    total = sum(numbers)
    count = len(numbers)
    return total / count

  return add

average = averager()
print(average(10)) # 10
print(average(20)) # 15

print('Use closure - rewrite')
def averager():
  total = 0
  count = 0

  def add(number):
    nonlocal total
    nonlocal count
    total += number
    count += 1
    return total / count

  return add

average = averager()
print(average(10)) # 10
print(average(20)) # 15

# Timer
print('Timer - class')
from time import perf_counter

class Timer:
  def __init__(self):
    self.start = perf_counter()

  def __call__(self):
    return perf_counter() - self.start

  def poll(self):
    return perf_counter() - self.start

timer = Timer()
print(timer.poll())
print(timer())

print('Timer - function')
def timer_func():
  start = perf_counter()

  def poll():
    return perf_counter() - start

  return poll

timer = timer_func()
print(timer())

# Counter
print('Counter')
def counter(initial_value=0):
  def inc(increment=1):
    nonlocal initial_value
    initial_value += increment
    return initial_value
  
  return inc

count = counter()
print(count()) # 1
print(count()) # 2
print(count()) # 3

print('---')
def outer(fn):
  count = 0

  def inner(*args, **kwargs):
    nonlocal count
    count += 1
    print(f'{fn.__name__} has been called {count} times')
    return fn(*args, **kwargs)

  return inner

def add(a, b):
  return a + b

counter_add = outer(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)
print(counter_add(10, 20))

# Counter with dict
print('Conter with dict')
def add(a, b):
  return a + b

def mult(a, b):
  return a * b

counters = dict()

def outer(fn):
  count = 0

  def inner(*args, **kwargs):
    nonlocal count
    count += 1
    counters[fn.__name__] = count
    return fn(*args, **kwargs)
  
  return inner

counter_add = outer(add)
counter_mult = outer(mult)
print(counter_add(10, 20)) # 30
print(counter_add(10, 20)) # 30
print(counter_mult(10, 20)) # 200
print(counters)

add = outer(add)
print(add(1, 2)) # 3
print(add(1, 2)) # 3
print(counters)