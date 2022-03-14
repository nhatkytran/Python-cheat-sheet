def logged(fn):
  from functools import wraps
  from datetime import datetime, timezone

  @wraps(fn)
  def inner(*args, **kwargs):
    run_dt = datetime.now(timezone.utc)
    result = fn(*args, **kwargs)
    print('{0}: called {1}'.format(run_dt, fn.__name__))
    return result

  return inner

@logged
def add(a, b):
  return a + b

print(add(1, 2))
# 2022-02-20 22:49:13.857117+00:00: called add
# 3

def timed(fn):
  from functools import wraps
  from time import perf_counter

  @wraps(fn)
  def inner(*args, **kwargs):
    start = perf_counter()
    result = fn(*args, **kwargs)
    end = perf_counter()
    print('{0} ran for {1:.6f}s'.format(fn.__name__, end - start))
    return result

  return inner

@timed
def mult(a, b):
  return a * b

print(mult(1, 2))
# mult ran for 0.000001s
# 2

# 2 decorators
print('Use 2 decorators at one time')
@logged
@timed
def fact(n):
  from operator import mul
  from functools import reduce

  return reduce(mul, range(1, n + 1))

# fact = logged(timed(fact))
print(fact(3))
# fact ran for 0.000008s
# 2022-02-20 23:06:50.804162+00:00: called fact
# 6