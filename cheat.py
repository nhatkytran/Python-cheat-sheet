# ——— General structure of usage ———
# Function that receives a function, its argument and
# launches the function with this argument
def apply_func(fn: 'function',
               x : 'any single argument'):
    return fn(x)
 
print(apply_func(lambda x: x*2, 3))              #> 6
print(apply_func(lambda st: st.upper(), 'abc'))  #> ABC
# Complication of the previous example
def apply_func(fn,
               *args   : 'any number of positional arguments',
               **kwargs: 'any number of keyword arguments'):
    return fn(*args, **kwargs)
 
def fn1(*args, **kwargs):
    print('args  :', args)           # show received positional arguments
    print('kwargs:', kwargs)         # show received keyword arguments
 
apply_func(fn1, 1, 2, 3, x4=10, x5=20)
#> args  : (1, 2, 3)
#> kwargs: {'x4': 10, 'x5': 20}

# //////////////////////////////////////////////////////////////////////
# ——— General structure of usage ———
# Sorting a list of characters case-insensitive
ls = ['c', 'B', 'D', 'a']
 
sorted_ls = sorted(ls, key = str.upper)
 
print(sorted_ls)                     #> ['a', 'B', 'c', 'D']
# Sorting a dictionary based on values
dict = {'def':300, 'abc':200, 'ghi':100}
 
sorted_list = sorted(dict, key = lambda e: dict[e])  # 'sorted' always returns a list
 
print(sorted_list)                   #> ['ghi', 'abc', 'def']
# Sorting a list of complex numbers based on distance from origin
comp_numbers = [3 - 4j, 2 + 3j, 10 + 10j]
 
sorted_comp2 = sorted(comp_numbers, key=lambda c: c.real**2 + c.imag**2)
 
print(sorted_comp2)                  #> [(2+3j), (3-4j), (10+10j)]
# Randomize the list via sorted function
from random import random
 
ls_ordered = [10, 20, 30, 40, 50]
 
ls_random = sorted(ls_ordered, key=lambda x: random())
 
print(ls_random)                     #> [20, 40, 50, 10, 30]  (as example)

# //////////////////////////////////////////////////////////////////////
# ——— Map, Filter, Zip ———
# map: calculation square of numbers
ls = [0, 1, 2, 3]
 
print(map(lambda x: x*x, ls))        #> <map object at 0x…>
print(list(map(lambda x: x*x, ls)))  #> [0, 1, 4, 9]
# filter: finding odd numbers in a list
ls = [-1, 0, 1, 2, 3]
 
print(filter(lambda x: x % 2, ls))        #> <filter object at 0x…>
print(list(filter(lambda x: x % 2, ls)))  #> [-1, 1, 3]
# warning:
print(list(filter(None, ls)))
#> [-1, 1, 2, 3] -0 is skipped because 0 is equivalent to False
# zip: aggregate numbers in lists
ls1 = [1, 2, 3]
ls2 = [10, 20, 30, 40]
 
print(list(zip(ls1, ls2)))                #> [(1, 10), (2, 20), (3, 30)]
# zip + list comprehension: pairwise addition of numbers in lists
# (numbers without a pair will be discarded)
ls1 = [1, 2, 3]
ls2 = [10, 20, 30, 40]
 
print([x + y for x, y in zip(ls1, ls2)])  #> [11, 22, 33]

# //////////////////////////////////////////////////////////////////////
# ——— Reduce ———
from functools import reduce
# reduce: finding sum of all numbers in a list
ls = [1, 2, 3]
print(reduce(lambda a, b: a+b, ls))                #> 6
# reduce: finding maximum value in a list
ls = [5, 8, 6, 10, 9]
print(reduce(lambda a, b: a if a > b else b, ls))  #> 10
# implementation of factorial via reduce
def fact(n):
    return reduce(lambda a,b: a*b, range(1, n+1), 1)  # 1 is initial value
 
print(fact(0))                                     #> 1
print(fact(1))                                     #> 1
print(fact(5))                                     #> 120

# //////////////////////////////////////////////////////////////////////
# ——— Partial functions ———
from functools import partial
 
def my_func(a, b, c):
    print(f'a={a}, b={b}, c={c}')
 
f1 = partial(my_func, 10, 20)
 
f1(30)
#> a=10, b=20, c=30
# sorting a list of 2D-points according their distance from origin (0, 0)
origin = (0, 0)
ls = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]
 
find_dist = lambda a,b: (a[0]-b[0])**2 + (a[1]-b[1])**2  # function of finding distance
                                                         # from origin
 
# way 1
dist_from_origin = partial(find_dist, origin)
print(sorted(ls, key=dist_from_origin))  #> [(0, 0), (1, 1), (0, 2), (-3, 2), (10, 10)]
 
# way 2
f2 = lambda x: find_dist(origin, x)
print(sorted(ls, key=f2))                #> [(0, 0), (1, 1), (0, 2), (-3, 2), (10, 10)]

# //////////////////////////////////////////////////////////////////////
# ——— The operator module ———
# Replacement of lambda for high-order functions. Just for convenience.
# Documentation: docs.python.org/3/library/operator.html
import operator
dir (operator)
#> list of accessible methods
# E.g., finding sum of all numbers in a list (via lambda-function and operator-module)
ls = [1, 2, 3]
print(reduce(lambda a, b: a+b, ls))            #> 6
print(reduce(operator.add, ls))                #> 6
ls = [10, 20, 30, 40]
 
# operator.getitem(a, b) returns the value of a at index b.
print(operator.getitem(ls, 1))  #> 20   # equivalent to print(ls[1])
 
# operator.setitem(a, b) sets the value of a at index b
operator.setitem(ls, 1, 'A')            # equivalent to ls.insert(1, 'A')
print(ls)                       #> [10, 'A', 30, 40]
 
# operator.delitem(a, b) removes the value of a at index b
operator.delitem(ls, 2)                 # equivalent to  del ls[2]
print(ls)                       #> [10, 'A', 40]

# operator.itemgetter takes a sequence object (such as list, tuple, string) and returns a value that is located in according index (or a tuple with such values)
ls = [10, 20, 30, 40]
st = 'Python'
 
# get the second element in sequence
f1 = operator.itemgetter(1)
print(f1(ls))                         #> 20
print(f1(st))                         #> y
 
# get the first and the last elements in sequence
f2 = operator.itemgetter(0, -1)
print(f2(ls))                         #> (10, 40)
print(f2(st))                         #> ('P', 'n')

# operator.attrgetter is similar to operator.itemgetter but retrieves object attributes
class MyClass:
    def __init__(self):
        self.a = 'attribute_a'
        self.b = 'attribute_b'
        self.c = 'attribute_c'
 
obj = MyClass()
 
atr_b = operator.attrgetter('b')
print(atr_b(obj))                       #> attribute_b
 
atr_ac = operator.attrgetter('a', 'c')
print(atr_ac(obj))                      #> ('attribute_a', 'attribute_c')
ls = [5-10j, 3+3j, 2-100j]
 
# extracting real and imaginary part of complex numbers
# (via direct attribute and using operator.attrgetter)
real_numbers1 = [n.real for n in ls]
real_numbers2 = [operator.attrgetter('real')(n) for n in ls]
print(real_numbers1)                                #> [5.0, 3.0, 2.0]
print(real_numbers2)                                #> [5.0, 3.0, 2.0]
 
real_imag1 = [n.imag for n in ls]
real_imag2 = [operator.attrgetter('imag')(n) for n in ls]
print(real_imag1)                                   #> [-10.0, 3.0, -100.0]
print(real_imag2)                                   #> [-10.0, 3.0, -100.0]
 
# sorting list based on real part of numbers (via lambda and using operator.attrgetter)
print(sorted(ls, key=lambda x: x.real))             #> [(2-100j), (3+3j), (5-10j)]
print(sorted(ls, key=operator.attrgetter('real')))  #> [(2-100j), (3+3j), (5-10j)]

# operator.methodcaller is essentially operator.attrgetter with auto-calling
# [we can not write additional ()]
st = 'Python'
print(operator.attrgetter('upper')(st)())  #> PYTHON
print(operator.methodcaller('upper')(st))  #> PYTHON