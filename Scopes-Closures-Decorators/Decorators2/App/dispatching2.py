# from numbers import Integral
# from html import escape

# def singledispatch(fn):
#   registry = {}
#   registry[object] = fn

#   def decorated(arg):
#     return registry.get(type(arg), registry[object])(arg)

#   def register(type_):
#     def inner(fn):
#       registry[type_] = fn
#       return fn
#     return inner

#   def dispatch(type_):
#     return registry.get(type_, registry[object])

#   decorated.register = register
#   # decorated.registry = registry
#   decorated.dispatch = dispatch
#   return decorated

# @singledispatch
# def htmlize(a):
#   return escape(str(a))

# # print(htmlize(10)) 10

# @htmlize.register(Integral)
# def html_integral_number(a):
#   return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

# # print(isinstance(10, Integral)) True
# # print(htmlize(10)) 10
# # => Complicated to fix

# from collections.abc import Sequence

# @htmlize.register(Sequence)
# def html_sequence():
#   items = ('<li>{0}</li>'.format(htmlize(item)) for item in l)
#   return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# # print(htmlize([1, 2, 3])) [1, 2, 3]

# //////////////////////////////////////////////////////
from html import escape
from numbers import Integral
from collections.abc import Sequence
from functools import singledispatch

@singledispatch
def html_lize(a):
  return escape(str(a))

# print(html_lize.registry)
# {<class 'object'>: <function html_lize at 0x10089e680>}
# print(html_lize.dispatch(str))
# <function html_lize at 0x10f346710>

@html_lize.register(Integral)
def html_integral_number(a):
  return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

# print(html_lize.registry)
# {<class 'object'>: <function html_lize at 0x10eb66680>, <class 'numbers.Integral'>: <function html_integral_number at 0x10ec743a0>}
# print(html_lize.dispatch(int))
# <function html_integral_number at 0x10ec743a0>

# Why it works?
# print(type(10)) <class 'int'>
# print(isinstance(10, int)) True
# print(isinstance(10, Integral)) True
# print(isinstance(True, Integral)) True

# print(html_lize.dispatch(bool)) <function html_integral_number at 0x104ee4ca0>

# print(html_lize(10)) 10(<i>0xa</i>)
# print(html_lize(True)) True(<i>0x1</i>)

@html_lize.register(Sequence)
def html_sequence(l):
  items = ('<li>{0}</li>'.format(html_lize(item)) for item in l)
  return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# print(html_lize([1, 2, 3]))
# <ul>
# <li>1</li>
# <li>2</li>
# <li>3</li>
# </ul>

# print(html_lize((1, 2, 3)))
# <ul>
# <li>1</li>
# <li>2</li>
# <li>3</li>
# </ul>

# => Problem
# print(isinstance('Python', Sequence)) True
# print(html_lize('Python'))
# maximum recursion depth exceeded while calling a Python object

# => Python is a Sequence
# for s in 'Python':
#   print(s)
# P
# y
# t
# h
# o
# n

def html_escape(a):
  return escape(str(a))

@html_lize.register(str)
def html_str(s):
  return html_escape(s).replace('\n', '<br/>\n')

# print(html_lize('Python 1 < 100')) Python 1 &lt; 100

# //////////////////////////////////////////////////////
@html_lize.register(tuple)
def html_tuple(t):
  items = (escape(str(item)) for item in t)
  return '{0}'.format(', '.join(items))

# print(html_lize((1, 2, 3))) 1, 2, 3

# @html_lize.register(tuple)
# def _(t):
#   items = (escape(str(item)) for item in t)
#   return '{0}'.format(', '.join(items))