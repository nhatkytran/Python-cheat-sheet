# I tried to use closures and decorators in real application but I found that for me it's enough difficult to understand what's happening then suddenly errors occur, I'm not a programmer. So I reconsider the contents of this section and made summary. I hope this is not bad if I publish it.

# ———  Different scopes  ———
a = 'global variable a'
b = 'global variable b'
c = 'global variable c'
d = 'global variable d'
e = 'global variable e'
 
def outer_func():
    a = 'outer_func a'
    b = 'outer_func b'
    c = 'outer_func c'
    d = 'outer_func d'
    # e - not mentioned
    
    def inner_func():
        global a
        nonlocal b
        c = 'inner_func c'
        # d - not mentioned: we can read it
        #     but attempt assign to it create local variable
        # nonlocal e → error
        print(a, b, c, d, sep='\n')
 
    inner_func()
 
outer_func()
#> global variable a
#> outer_func b
#> inner_func c
#> outer_func d

# ———  Closures  ———
# Simplest closure
def outer():
    x = 'Python'                # 'x' → free variable
    def inner():                # 'inner()' → inner function
        print(f'{x} rocks!')    # 'inner()' + 'x' → closure
    return inner                # "returning" a closure
 
fn = outer()
 
fn()                            #> Python rocks!
fn()                            #> Python rocks!
 
print(fn.__closure__)           #> (<cell at 0x…: str object at 0x…>,)
print(fn.__code__.co_freevars)  #> ('x',)
# outer.x and inner.x point to intermediary cell, that in its turn point to common value. Therefore, if x changes it changes simultaneously for both scopes.

# Simplest closure with changeable free variable
def outer():
    x = 'Python'
    n = 0
    def inner():
        nonlocal n
        n += 1
        print(f'{x} rocks! -{n}')
    return inner
 
fn1 = outer()
fn2 = outer()
 
fn1()                            #> Python rocks! -1
fn1()                            #> Python rocks! -2
 
fn2()                            #> Python rocks! -1
fn2()                            #> Python rocks! -2
 
print(fn1.__closure__)           #> (<cell at 0x…: int object at 0x…>,
                                 #>  <cell at 0x…: str object at 0x…>)
print(fn1.__code__.co_freevars)  #> ('n', 'x')
# Closure returning 2 functions with common free variable
def outer():
    count = 0
    
    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count
    
    return inc1, inc2
 
g1, g2 = outer()
print(g1(), g1(), g2(), g1())  #> 1 2 3 4
# Closure with settable during run-time initial value of a free variable
def adder(n):
    def inner(x):
        return x+n
    return inner
 
add_from_10 = adder(10)
add_from_20 = adder(20)
 
print( add_from_10(5) )  #> 15
print( add_from_20(5) )  #> 25

# POTENTIAL DANGER with unintentional closure
adders = []
 
for n in range(10,40,10):
    adders.append(lambda x: x+n)
 
for adr in adders:
    print(adr(5))
#> 35
#> 35
#> 35
 
n = 100
for adr in adders:
    print(adr(5))
#> 105
#> 105
#> 105
# correction of the previous code
adders = []
 
for n in range(10,40,10):
    adders.append(lambda x, *, start=n: start+x)
 
for adr in adders:
    print(adr(5))
#> 15
#> 25
#> 35
 
# but caution for such case
for adr in adders:
    print(adr(5, start=60))
#> 65
#> 65
#> 65

# nested closure
def incrementer(start):
    
    # inner + start → outer closure
    def inner(n):
        current = start
        
        # inc + n + start → nested closure
        def inc():
            nonlocal current
            current += n
            return current
 
        return inc
    
    return inner
 
inc_from_100 = incrementer(100)
inc_2_from_100 = inc_from_100(2)
 
print(inc_2_from_100())  #> 102
print(inc_2_from_100())  #> 104

# ———  Decorators  ———
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        """ This is the inner function """
        nonlocal count
        count += 1
        print(f"Function '{fn.__name__}' has been called {count} times")
        return fn(*args, **kwargs)
    return inner
 
@counter                                 # add = counter(add)
def add(a:int, b:int=0):
    """ Add two values """
    return a + b
 
 
print(add(10,20))
#> Function 'add' has been called 1 times
#> 30
 
print(add(30,40))
#> Function 'add' has been called 2 times
#> 70
 
 
# But without 'wrapper' such function has flaws in documentation:
print(add.__name__)
#> inner
 
help(add)
#> Help on function inner in module __main__:
#> inner(*args, **kwargs)
#>     This is the inner function
 
print(add.__doc__)
#>  This is the inner function 

# Using wrapper:
from functools import wraps
 
def counter(fn):
    count = 0
    @wraps(fn)                           # inner = wraps(fn)(inner)
    def inner(*args, **kwargs):
        """ This is the inner function """
        nonlocal count
        count += 1
        print(f"Function '{fn.__name__}' has been called {count} times")
        return fn(*args, **kwargs)
    return inner
 
@counter                                 # mult = counter(mult)
def mult(a:int, b:int=1):
    """ Multiply two values """
    return a + b
 
 
print(mult.__name__)
#> mult
 
help(mult)
#> Help on function mult in module __main__:
#> mult(a: int, b: int = 1)
#>     Multiply two values
 
print(mult.__doc__)
#> Multiply two values 

# Memoization of recursive function with limited cache:
from functools import lru_cache   # lru - abbr. from 'least recently used'
 
@lru_cache(maxsize=8)  # by default 128,
                       # more efficient to use the power of 2,
                       # None - unlimited cache
def fib(n):
    print(f'calculating fib({n})')
    return 1 if n<=2 else fib(n-1) + fib(n-2)
 
fib(12)                # all values calculated
fib(5)                 # value is taken from cache
fib(4)                 # all values calculated again

# //////////////////////////////////////////////////////////////////
# ——— Decorators in general form ———
# simplest decorator
def dec(fn):
    print("running dec")
    
    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)
    
    return inner
 
 
@dec                         # f1 = dec(f1)
def f1():
    print("running f1")
#> running dec
 
f1()
#> running inner
#> running f1

# decorator factory (decorator with parameter)
def dec_factory(n):
    print("running dec_factory")
    
    def dec(fn):
        print(f"running dec with parameter n={n}")
 
        def inner(*args, **kwargs):
            print("running inner")
            return fn(*args, **kwargs)
 
        return inner
 
    return dec
 
 
@dec_factory(10)             # f2 = dec_factory(10)(f2)
def f2():
    print("running f2")
#> running dec_factory
#> running dec with parameter n=10
 
f2()
#> running inner
#> running f2

# Decoration via class (with parameter)
class DecClass:
    def __init__(self, n):
        print('running DecClass')
        self.n = n
    
    def __call__(self, fn):
        print(f'running __call__ with parameter n={self.n}')
        def inner(*args, **kwargs):
            print('running inner')
            return fn(*args, **kwargs)
        return inner
 
 
@DecClass(10)
def f3():
    print('running f3') 
#> running DecClass
#> running __call__ with parameter n=10
 
f3()
#> running inner
#> running f3

# //////////////////////////////////////////////////////////////////
# ——— Decorating classes ———
# (adding to classes new functional)
# Simplest example
class Crow:
    pass
 
def speak(cls):
    cls.speak = lambda self, msg: f'{self.__class__.__name__} says: {msg}'
    return cls
 
Crow = speak(Crow)
 
 
cr = Crow()
print(cr.speak('Kah'))  #> Crow says: Kah

# Extracting infomation about an object via applying decorator to a class
def info(self):
    results = []
    results.append(f'class: {self.__class__.__name__}')
    for k,v in vars(self).items():
        results.append(f'{k}: {v}')
    return results
 
def debug_info(cls):
    cls.debug = info
    return cls      # we return the class only for using decorator syntax
 
@debug_info         # Person = debug_info(Person)
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
 
 
p = Person('Xena', 1995)
p.debug()
#> ['class: Person', 'name: Xena', 'birth_year: 1995']
