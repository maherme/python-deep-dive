#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:35:44 2021

@author: maherme
"""
#%%

from collections import namedtuple

Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(10, 20)

# This will give an error:
pt.x = 100
pt[0] = 100

#%%
# We can create another tuple:
print(pt)
print(id(pt))
pt = Point2D(100, pt.y)
print(pt)
print(id(pt))

#%%
# Let see with a more complicated tuple:

Stock = namedtuple('Stock', 'symbol year month day open high low close')
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(djia)

djia = Stock(djia.symbol, djia.year, djia.month, djia.day, 
             djia.open, djia.high, djia.low, 1000)

print(djia)

#%%
# This is too much typing, let try in a better way using unpacking:
    
*values, _ = djia
print(values)
values.append(26_393)
print(values)
djia = Stock(*values)
print(djia)

#%%
# Other way to do this is using slicing:
    
values = djia[:7]
print(values)
values + (100,)
djia = Stock(*(values + (100,)))
print(djia)
# Other way:
djia = Stock(*values, 1000)
print(djia)

#%%
# But the above way does not work fine with values in the middle, so we can
# use _replace method:

print(id(djia))
djia = djia._replace(year=2019, open=10000)
print(id(djia))
print(djia) # Notice this creates a new tuple

#%%
# We can also use _make method:

djia = Stock._make(values + (100 ,))
print(djia)

#%%
# For creating an extended tuple:

print(Point2D._fields)
print(Point2D._fields + ('z',))
Point3D = namedtuple('Point3D', Point2D._fields + ('z', ))
print(Point3D._fields)

print(Stock._fields)
StockExt = namedtuple('StockExt', Stock._fields + ('previous_close', ))
print(StockExt._fields)

#%%

print(pt)
pt3d = Point3D(*pt, 100)
print(pt3d)

print(djia)
djia_ext = StockExt(*djia, 1_000_000)
print(djia_ext)

#%%