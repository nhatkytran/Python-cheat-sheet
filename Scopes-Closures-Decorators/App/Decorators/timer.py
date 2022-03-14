#  0, 1, 1, 2, 3, 5,...
# Recursion
def recursion_fib(n):
  if n <= 2:
    return 1
  else:
    return recursion_fib(n - 1) + recursion_fib(n - 2)

#  Loop
def loop_fib(n):
  f0 = 0
  f1 = 1

  for i in range(2, n + 1):
    f0, f1 = f1, f0 + f1

  return f1

# Timer
def timer(fn):
  from time import perf_counter
  from functools import wraps

  @wraps(fn)
  def inner(*args, **kwargs):
    start = perf_counter()
    result = fn(*args, **kwargs)
    end = perf_counter()
    elapsed = end - start

    args_ = [str(a) for a in args]
    kwargs_ = ['{0} = {1}'.format(k, v) for (k, v) in kwargs.items()]
    all_args = args_ + kwargs_
    args_str = ','.join(all_args)

    print('{0}({1}) took {2:.6f} to run.'.format(fn.__name__, args_str, elapsed))
    return result

  return inner

@timer
def fib_recursion(n):
  return recursion_fib(n)

print(fib_recursion(2))

print('---')
loop_fib = timer(loop_fib)
print(loop_fib(2))

print('---')
# Use reduce
print('Reduce----------')
from functools import reduce
# 0, 1, 1, 2, 3, 5, 8
# 0, 1, 2, 3, 4, 5, 6
@timer
def fib_reduce(n):
  initial = (1, 0)
  dummy = range(n)
  fib_n = reduce(lambda a, b: (a[0] + a[1], a[0]), dummy, initial)
  
  return fib_n[1]

print(loop_fib(35))
print(fib_reduce(35))

# Loop is the fastest