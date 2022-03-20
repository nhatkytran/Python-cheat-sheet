from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(10, 20)

# pt.x = 100
# AttributeError: can't set attribute

# print(id(pt))
# 4365297856

pt = Point2D(100, pt.y)

# print(id(pt))
# 4365554816

# => Tuple is similar to a string

# //////////////////////////////////////
Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26313, 26458, 26260, 26393);

*values, _ = djia
djia = Stock(*values, 1000)

# print(djia)
# Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=1000)

# //////////////////////////////////////
# a = [1, 2, 3]
# print(id(a))
# 4404848960
# a = a + [4, 5]
# print(id(a))
# 4404853440

# a = [1, 2, 3]
# print(id(a))
# a.append(4)
# print(id(a))
# => 4346866240

# a = [1, 2, 3]
# print(id(a))
# a.extend([4, 5])
# print(id(a))
# => 4326877760

# //////////////////////////////////////
# nametuple with _replace
Stock = namedtuple('Stock', 'symbol year month day open high low close')

# djia = Stock('DJIA', 2018, 1, 25, 26313, 26458, 26260, 26393)
# print(id(djia))
# 4486164464
# djia = djia._replace(year=2022)
# print(id(djia))
# 4486164576
# => Seems like _replce method just replaces values of a tuple but actually, _replace creates a new tuple

# //////////////////////////////////////
# nametuple with _make
Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26313, 26458, 26260, 26393);

# values = djia[:7]
# new_values = values + (1000, )
# djia = Stock._make(new_values)
# print(djia)
# Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=1000)

# //////////////////////////////////////
# nametuple with _fields
Point2D = namedtuple('Point2D', 'x y')
# print(Point2D._fields)
# ('x', 'y')

Point3D = namedtuple('Point3D', Point2D._fields + ('z', ))
# print(Point3D._fields)
# ('x', 'y', 'z')

# //////////////////////////////////////
pt2d = Point2D(10, 20)
# print(pt2d)
# Point2D(x=10, y=20)

pt3d = Point3D(*pt2d, 30)
# print(pt3d)
# Point3D(x=10, y=20, z=30)
