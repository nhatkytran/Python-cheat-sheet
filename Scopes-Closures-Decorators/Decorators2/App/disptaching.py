# Dispatching
# Overloading
# Know type of arguments passed in

from html import escape

def html_escape(arg):
  return escape(str(arg))
# print(html_escape('<i>hi</i>'))
# &lt;i&gt;hi&lt;/i&gt;

def html_int(a):
  return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))
# print(html_int(10))
# 10(<i>0xa</i>)

def html_real(a):
  return '{0:.2f}'.format(round(a, 2))
# print(html_real(5.1111))
# 5.11

def html_str(s):
  return html_escape(s).replace('\n', '<br/>\n')
# print(html_str('<strong>Frlix</strong>'))

def html_list(l):
  items = ('<li>{0}</li>'.format(html_escape(item)) for item in l)
  return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_set(s):
  return html_list(s)

def html_dict(d):
  items = ('<li>{0}={1}</li>'.format(k, v) for k, v in d.items())
  return '<ul>\n' + '\n'.join(items) + '\n</ul>'

from decimal import Decimal

def htmlize(arg):
  if isinstance(arg, int):
    return html_int(arg)
  elif isinstance(arg, float) or isinstance(arg, Decimal):
    return html_real(arg)
  elif isinstance(arg, str):
    return html_str(arg)
  elif isinstance(arg, list) or isinstance(arg, tuple):
    return html_list(arg)
  elif isinstance(arg, dict):
    return html_dict(arg)
  elif isinstance(arg, set):
    return html_set(arg)
  else:
    return html_escape(arg)

# print(htmlize(100))
# 100(<i>0x64</i>)

# print("""Python
# rocks!
# """)

# print(htmlize([1, 2, 3]))
# <ul>
# <li>1</li>
# <li>2</li>
# <li>3</li>
# </ul>

# ////////////////////////////////
def htmlize(arg):
  registry = {
    object: html_escape,
    int: html_int,
    float: html_real,
    Decimal: html_real,
    str: html_str,
    list: html_list,
    tuple: html_list,
    set: html_set,
    dict: html_dict
  }
  
  fn = registry.get(type(arg), registry[object])
  return fn(arg)

# print(htmlize(100))
# 100(<i>0x64</i>)

# /////////////////////////////////////////////////
# Part 2
from html import escape

def singledispatch(fn):
  registry = {}
  registry[object] = fn

  def inner(arg):
    return registry[object](arg)

  return inner

@singledispatch
def htmlize(a):
  return escape(str(a))

# print(htmlize('1 < 100')) 1 &lt; 100

# /////////////////////////////////////////////////
from html import escape

def singledispatch(fn):
  registry = {}
  registry[object] = fn
  registry[int] = lambda a: '{0}(<i>{1}</i>)'.format(a, str(hex(a)))
  registry[str] = lambda a: html_escape(s).replace('\n', '<br/>\n')

  def inner(arg):
    return registry.get(type(arg), registry[object])(arg)

  return inner

@singledispatch
def htmlize(a):
  return escape(str(a))

# print(htmlize(100)) 100(<i>0x64</i>)

# /////////////////////////////////////////////////
from html import escape

def singledispatch(fn):
  registry = {}
  registry[object] = fn

  def decorated(arg):
    return registry.get(type(arg), registry[object])(arg)

  def register(type_):
    def inner(fn):
      registry[type_] = fn
      return fn
    return inner

  def dispatch(type_):
    return registry.get(type_, registry[object])

  decorated.register = register
  # decorated.registry = registry
  decorated.dispatch = dispatch
  return decorated

@singledispatch
def htmlize(a):
  return escape(str(a))

# print(htmlize('1 < 100')) 1 &lt; 100
# print(htmlize.registry)
# {<class 'object'>: <function htmlize at 0x10d322c20>}
# print(htmlize.dispatch(int)) <function htmlize at 0x10dfbac20>

@htmlize.register(int)
def html_int(a):
  return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

# print(htmlize(100)) 100(<i>0x64</i>)
# print(htmlize.registry)
# {<class 'object'>: <function htmlize at 0x10f5e6c20>, <class 'int'>: <function html_int at 0x10f649480>}
# print(htmlize.dispatch(int)) <function html_int at 0x103e5d480>

@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
  items = ('<li>{0}</li>'.format(html_escape(item)) for item in l)
  return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# print(htmlize([1, 2, 3]))
# print(htmlize((1, 2, 3)))
# <ul>
# <li>1</li>
# <li>2</li>
# <li>3</li>
# </ul>
# print(htmlize.registry)
# {<class 'object'>: <function htmlize at 0x10734ac20>, <class 'int'>: <function html_int at 0x1073ad480>, <class 'list'>: <function html_sequence at 0x1073ad3f0>, <class 'tuple'>: <function html_sequence at 0x1073ad3f0>}

# /////////////////////////////////////////////////
# print(htmlize(True)) True
# print(type(True)) <class 'bool'>
# print(isinstance(True, bool)) True
# Important: isinstance works with sub-classes as well

# class Person():
#   pass

# class Student(Person):
#   pass

# p = Student()

# print(type(p)) <class '__main__.Student'>
# print(isinstance(Student, Person)) False
# print(isinstance(p, Student)) True
# print(isinstance(p, Person)) True

from numbers import Integral
from html import escape

def singledispatch(fn):
  registry = {}
  registry[object] = fn

  def decorated(arg):
    return registry.get(type(arg), registry[object])(arg)

  def register(type_):
    def inner(fn):
      registry[type_] = fn
      return fn
    return inner

  def dispatch(type_):
    return registry.get(type_, registry[object])

  decorated.register = register
  # decorated.registry = registry
  decorated.dispatch = dispatch
  return decorated

@singledispatch
def htmlize(a):
  return escape(str(a))

# print(htmlize(10)) 10

@htmlize.register(Integral)
def html_integral_number(a):
  return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

# print(isinstance(10, Integral)) True
# print(htmlize(10)) 10
# => Complicated to fix

@htmlize.register(int)
@htmlize.register(bool)
def html_integral_number(a):
  return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

# /////////////////////////////////////////////////
# print(htmlize(10)) 10(<i>0xa</i>)
# print(htmlize(True)) True(<i>0x1</i>)

# /////////////////////////////////////////////////
# The same issue as above
from collections.abc import Sequence

@htmlize.register(Sequence)
def html_sequence():
  items = ('<li>{0}</li>'.format(html_escape(item)) for item in l)
  return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# print(htmlize([1, 2, 3])) [1, 2, 3]