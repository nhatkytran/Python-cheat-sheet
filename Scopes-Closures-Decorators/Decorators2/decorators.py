# The timed decorator

def timed(fn, n):
  from time import perf_counter

  def inner(*args, **kwargs):
    total_elapsed = 0
    
    for i in range(n):
      start = perf_counter()
      result = fn(*args, **kwargs)
      total_elapsed += (perf_counter() - start)
    
    average_elapsed = total_elapsed / n
    print(average_elapsed)

    return result
  
  return inner

# def add(a, b):
#   return a + b
# add = timed(add, 100)
# print(add(1, 2))

# ///////
# Decorator factory

def timed(n):
  def dec(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
      total_elapsed = 0
      
      for i in range(n):
        start = perf_counter()
        result = fn(*args, **kwargs)
        total_elapsed += (perf_counter() - start)
      
      average_elapsed = total_elapsed / n
      print(average_elapsed)

      return result
    return inner
  return dec

# def mult(a, b):
#   return a * b

# mult = timed(100)(mult)
# print(mult(1, 2))

@timed(100)
def mult(a, b):
  return a * b

print(mult(1, 2))

def test(a):
  def test():
    return a
  return test

print(test)
print(test(10))