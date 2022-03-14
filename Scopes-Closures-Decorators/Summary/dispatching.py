# I think that I'm not the single person who had trouble with understanding of the last 3 lectures. So I decide to make summary of basic moments. I hope that it will help someone.
# I. Our implementation
from html import escape
def singledispatch(fn):
    registry = {object: fn}   # initial dictionary
    
    def decorated(arg):
        """ Choose applied function according type of given argument """
        f = registry.get(type(arg), registry[object])
        return f(arg)
        
    def register(type_):
        """ Register new couple 'type: function' """
        def inner(fn):
            registry[type_] = fn
            return fn              # we need this return for stacking register recorators
        return inner
 
    def dispatch(type_):
        """ Allow user to check what function is used for given type """
        return registry.get(type_, registry[object])
    
    decorated.register = register
    decorated.registry = registry  # for security it's better don't open access,
                                   # only for debugging purpose
    decorated.dispatch = dispatch
        
    return decorated
# Set default couple 'object: function'
@singledispatch
def htmlize(a):             # htmlize now our default function, for object
    return escape(str(a))
htmlize.registry            # check content of inner dictionary 'registry'
#> {object: <function __main__.htmlize(a)>}
# register new couple 'type: function'
@htmlize.register(int)     # html_int = htmlize.register(int)(html_int)
def html_int(a):
    return f'{a}(<i>({hex(a)})</i>)'
htmlize.registry            # check content of inner dictionary 'registry' again
#> {object: <function __main__.htmlize(a)>,
#>  int:    <function __main__.html_int(a)>}
htmlize.dispatch(int)       # check what function is used for type 'int'
#> <function __main__.html_int(a)>
print(htmlize('0 < 1'))     # check of work 1
#> 0 &lt; 1
print(htmlize(255))         # check of work 2
#> 255(<i>(0xff)</i>)
# register simultaneously two couple 'type1: function1', 'type2: function1'
@htmlize.register(tuple)  # html_sequence = htmlize.register(tuple)(html_sequence)
@htmlize.register(list)   # html_sequence = htmlize.register(list)(html_sequence)
def html_sequence(ls):
    items = (f'<li>{htmlize(item)}</li>' for item in ls)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
htmlize.registry            # check content of inner dictionary 'registry'
#> {object: <function __main__.htmlize(a)>,
#>  int:    <function __main__.html_int(a)>,
#>  list:   <function __main__.html_sequence(ls)>,
#>  tuple:  <function __main__.html_sequence(ls)>}
print(htmlize([10, 20, 30]))  # check of work 3
#> <ul>
#> <li>10(<i>(0xa)</i>)</li>
#> <li>20(<i>(0x14)</i>)</li>
#> <li>30(<i>(0x1e)</i>)</li>
#> </ul>

# Our implementation is simplified and there're problems if, e.g., we try to use Integral and Sequence types.

# ———
# II. Implementation using module functools
from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from html import escape
# Set default couple 'object: function'
@singledispatch
def htmlize(a):             # htmlize now our default function, for object
    return escape(str(a))
htmlize.registry            # check content of inner dictionary 'registry'
#> mappingproxy({object: <function __main__.htmlize(a)>})
# register new couple 'type: function'
@htmlize.register(Integral)
def htmlize_integral_number(a):
    return f'{a}(<i>({hex(a)})</i>)'
htmlize.registry            # check content of inner dictionary 'registry' again
#> mappingproxy({object:           <function __main__.htmlize(a)>,
#>               numbers.Integral: <function __main__.htmlize_integral_number(a)>})
htmlize.dispatch(int)       # check what function is used for type 'int'
#> <function __main__.htmlize_integral_number(a)>
print(htmlize('0 < 1'))     # check of work 1
#> 0 &lt; 1
print(htmlize(255))         # check of work 2
#> 255(<i>(0xff)</i>)
@htmlize.register(Sequence)  # html_sequence = htmlize.register(Sequence)(html_sequence)
def html_sequence(ls):
    items = (f'<li>{htmlize(item)}</li>' for item in ls)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
htmlize.registry            # check content of inner dictionary 'registry'
#> mappingproxy({object:                   <function __main__.htmlize(a)>,
#>               numbers.Integral:         <function __main__.htmlize_integral_number(a)>,
#>               collections.abc.Sequence: <function __main__.html_sequence(ls)>})
print(htmlize([10, 20, 30]))  # check of work 3
#> <ul>
#> <li>10(<i>(0xa)</i>)</li>
#> <li>20(<i>(0x14)</i>)</li>
#> <li>30(<i>(0x1e)</i>)</li>
#> </ul>

# Error then sequence is applied to string:
print(htmlize('python'))
#> RecursionError: maximum recursion depth exceeded
# Correction of aforementioned error 
@htmlize.register(str)
def html_str(s):
    return escape(str(s)).replace('\n', '<br/>\n')
print(htmlize('python'))   # check of work 4
#> python

# Malvina