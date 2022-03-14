# Global Scope and Local Scope
# ////////////////////////////////////
a = 10

def func():
  a = 100
  print(a)

func() # a = 100
print(a) # a = 10
# ////////////////////////////////////
a = 10

def func():
  print(a)

func() # a = 10
# ////////////////////////////////////
a = 10

def func():
  global a
  a = 100
  print(a)

func() # a = 100
print(a) # a = 100
# ////////////////////////////////////
def func():
  global b
  b = 1000

func()
print(b) # 1000
# ////////////////////////////////////
a = 10

def func():
  print(a)
  a = 100
  print(a)

# func() # Local variable "a" referenced before assignment
# ////////////////////////////////////
a = 10

func = lambda n: a ** n

print(func(2)) # 100
# ////////////////////////////////////
for i in range(10):
  x = i * 2

print(x) # x = 18
# ////////////////////////////////////
for i in range(10):
  continue

print(i) # i = 9

# List comprehension especially
[j for j in range(10)]

# print(j) # name "j" is not defined;
# ////////////////////////////////////
print('----------')
# Nonlocal scopes
# ////////////////////////////////////
x = 10

def outer():
  global x
  x = 100

outer()

print(x) # 100

x = 10

def outer():
  def inner():
    global x
    x = 1000

  inner()

outer()

print(x) # 1000
# ////////////////////////////////////
# Modifying nolocal
print('Modifying nonlocal variable')

x = 10

def outer():
  x = 100

  def inner():
    nonlocal x
    x = 1000
  
  inner()
  print(x) # x = 1000

outer()
print(x) # x = 10
# Especially with only nonlocal
# ////////////////////////////////////
# The chain of nonlocal
def outer():
  x = 10

  def inner():
    nonlocal x
    x = 20

    def super_inner():
      nonlocal x
      x = 30
    super_inner()
  inner()
  print(x)

outer() # 30
# ////////////////////////////////////
# This scene doesn't work
# x = 10
# 
# def outer():
#   global x
#   x = 20
#
#   def inner():
#     nonlocal x
#     x = 30
#   inner()
#
# outer()
#
# => Error: Can't find nonlocal variable "x"
