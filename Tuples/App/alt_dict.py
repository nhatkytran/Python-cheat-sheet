data_dict = dict(key1 = 100, key2 = 200, key3 = 300)

# print(data_dict)
# {'key1': 100, 'key2': 200, 'key3': 300}

# print(data_dict.keys())
# dict_keys(['key1', 'key2', 'key3'])
# print(data_dict.values())
# dict_values([100, 200, 300])

from collections import namedtuple

Data = namedtuple('Data', data_dict.keys())
d1 = Data(*data_dict.values())

# print(d1._fields) ('key1', 'key2', 'key3')

# print(d1)
# Data(key1=100, key2=200, key3=300)

# print(d1[0]) 100

# print(d1['key1']) TypeError: tuple indices must be integers or slices, not str
# print(d1.key1) 100

d2 = Data(key3 = 30, key2 = 20, key1 = 10)
# print(d2) Data(key1=10, key2=20, key3=30)
# => Keyword argument is prefered because it is more safer

# ///////////////////////////////////////////
# Transform a dictionary into a named tuple
data_dict = dict(key1 = 1, key2 = 2, key3 = 3)

from collections import namedtuple

DataReverse = namedtuple('DataReverse', data_dict.keys())
d = DataReverse(**data_dict)

# print(d)
# DataReverse(key1=1, key2=2, key3=3)

# print(d.key1) 1
# print(d['key1']) TypeError: tuple indices must be integers or slices, not str
# print(getattr(d, 'key1')) 1

# print(getattr(d, 'key0', 1)) 1
# key0 does not exist in d tuple => return 1

# ///////////////////////////////////////////
# Convert list of dicts to list of named tuples
data_list = [
  { 'key1': 1, 'key2': 2 },
  { 'key1': 3, 'key2': 4 },
  { 'key1': 5, 'key2': 6, 'key3': 7 },
  { 'key2': 100 }
]

# keys = {key for data_ in data_list for key in data_.keys()}
# print(keys) {'key1', 'key3', 'key2'}

keys = set()

for data_ in data_list:
  for key in data_.keys():
    keys.add(key)

# print(keys) {'key2', 'key3', 'key1'}

from collections import namedtuple

Struct = namedtuple('Struct', sorted(keys))

# print(Struct._fields) ('key1', 'key2', 'key3')

Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)

# print(Struct.__new__.__defaults__) (None, None, None)

tuple_list = []

for data_ in data_list:
  tuple_list.append(Struct(**data_))

# print(tuple_list)
# [Struct(key1=1, key2=2, key3=None), Struct(key1=3, key2=4, key3=None), Struct(key1=5, key2=6, key3=7), Struct(key1=None, key2=100, key3=None)]

# ///////////////////////////////////////////
data_list = [
  { 'key1': 1, 'key2': 2 },
  { 'key1': 3, 'key2': 4 },
  { 'key1': 5, 'key2': 6, 'key3': 7 },
  { 'key2': 100 }
]

def tuplify_dicts(dicts):
  from collections import namedtuple

  keys = {key for data_ in data_list for key in data_.keys()}
  Struct = namedtuple('Struct', sorted(keys), rename = True)
  Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)

  return [Struct(**data_) for data_ in data_list]

tuple_list = tuplify_dicts(data_list)

# print(tuple_list)
# [Struct(key1=1, key2=2, key3=None), Struct(key1=3, key2=4, key3=None), Struct(key1=5, key2=6, key3=7), Struct(key1=None, key2=100, key3=None)]