# Closures (function + free variables (extended scopes))
# ////////////////////////////////
def outer():
  x = 'Python'

  def inner():
    print(f'Hello {x}')
  
  return inner

fn = outer()
fn() # Hello Python
# ////////////////////////////////
# Python Cells and Multi-Scoped Variables
def outer():
  x = 'Python'

  def inner():
    print(x)
  
  return inner
# outer x and inner x => cell => str
# ////////////////////////////////
def outer():
  a = 10

  def inner():
    b = 20

    def super_inner():
      print(a, b)
    
    return super_inner
  return inner

fn = outer() # inner # super_inner
print('----------')
print(fn.__closure__)
print(fn.__code__.co_freevars) # ('a',) # ('a','b')
# ////////////////////////////////
# Modifying free variables
def outer():
  count = 0
  
  def inner():
    nonlocal count
    count += 1
    return count
  
  return inner

fn = outer()
print(fn()) # 1
print(fn()) # 2
print(fn()) # 3
# ////////////////////////////////
# Multiple instances of Closures
print('Multiple instances of Closures')
fn1 = outer()
fn2 = outer()

print(fn1()) # 1
print(fn1()) # 2
print(fn1()) # 3
print(fn2()) # 1
print(fn2()) # 2
print(fn2()) # 3
# ////////////////////////////////
# Shared extended scopes
print('Shared extended scopes')
def outer():
  count = 0

  def inner1():
    nonlocal count
    count += 1
    return count

  def inner2():
    nonlocal count
    count += 1
    return count

  return inner1, inner2

fn1, fn2 = outer()
print(fn1()) # 1
print(fn2()) # 2
# Noticeable trap in Shared extended scopes
print('Noticeable trap in Shared extended scopes')
def outer(n):
  def inner(x):
    return x + n
  return inner

fn1 = outer(1) # 11
fn2 = outer(2) # 12
fn3 = outer(3) # 13
print(fn1(10))
print(fn2(10))
print(fn3(10))
print('----------')

adders = []
for n in range(1, 4):
  adders.append(lambda x: x + n)

print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
# ////////////////////////////////
# Nested closures
def outer(n):
  def inner(start):
    current = start

    def super_inner():
      nonlocal current
      current += n
      return current
    
    return super_inner
  return inner

fn = outer(2)
super_fn = fn(100)
print(super_fn()) # 102
# ////////////////////////////////
#Using for loop to create function
adders = []
for n in range(1, 4):
  adders.append(lambda x, y=n: x + y)

print(adders[0](10)) # 11
print(adders[1](10)) # 12
print(adders[2](10)) # 13
