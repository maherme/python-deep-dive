#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 17:53:11 2021

@author: maherme
"""
#%%

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
from collections import namedtuple

Point2D = namedtuple('Point2D', ['x', 'y'])

pt1 = Point2D(10, 20)
print(pt1)

pt3d_1 = Point3D(10, 20, 30)
# As you  will see pt3d_1 representation does not look like pt1, we need to 
# add more code to the class Point3D to fix this.
print(pt3d_1)

#%%
# You can also create an instance giving the parameter names:
    
p = Point3D(x=10, y=20, z=30)
print(p)
print(isinstance(p, tuple))
p = Point2D(x=10, y=20)
print(p)
print(isinstance(p, tuple))

#%%

pt1 = Point2D(10, 20)
pt2 = Point2D(10, 20)
print(pt1 is pt2)
print(pt1 == pt2)

pt1 = Point3D(10, 20, 30)
pt2 = Point3D(10, 20, 30)
print(pt1 is pt2)
print(pt1 == pt2) # As Point3D is a class, the method eq need to be implemented

#%%

class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False
        
#%%

pt1 = Point3D(10, 20, 30)
print(pt1)
pt2 = Point3D(10, 20, 30)
print(pt2)
print(pt1 is pt2)
print(pt1 == pt2)

#%%
# Let try to find the maximum coordinate:
    
pt1 = Point2D(10, 20)
pt2 = Point3D(10, 20, 30)

max(pt1)
max(pt2) # This will fail because is not iterable, is not a tuple.

#%%
# Let implement a dot product.

def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

pt1 = Point3D(1, 2, 3)
pt2 = Point3D(1, 1, 1)

print(dot_product_3d(pt1, pt2))

#%%
# Implement for 2 coordinates.

a = (1, 2)
b = (1, 1)

list(zip(a, b))

sum(e[0] * e[1] for e in zip(a, b))

#%%
# Implement using a function.

def dot_product(a, b):
    return sum(e[0] * e[1] for e in zip(a, b))

print(dot_product(a, b))

pt1 = Point2D(1, 2)
pt2 = Point2D(1, 1)

print(dot_product(pt1, pt2))

#%%

Vector3D = namedtuple('Vector3D', 'x y z')
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(1, 1, 1)

print(dot_product(v1, v2))

#%%
# v1 is a tuple indeed:

print(tuple(v1))
print(v1[0])
print(v1[0:2])
print(v1)
# This is the advantage of a named tuple, you can choose if get a component as
# a tuple or as a class
print(v1.x)
print(v1.y)

#%%
# You can use as many spaces as you want to create the named tuple:

Circle = namedtuple('Circle', 'center_x center_y         radius')

c = Circle(0, 0, 10)
print(c)
print(c.radius)

#%%
# Let define a named tuple:

Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26_323, 26_458, 26_260, 26_393)

# You can access as a class:
print(djia)
print(djia.close)

# You can iterate:
for item in djia:
    print(item)
    
# You can unpack:
symbol, year, month, day, *_, close = djia
print(symbol, year, month, day, close)

#%%

# You can not use name starting with an underscore:
Person = namedtuple('Person', 'name age _ssn')

#%%

# You can fix this set rename = True:
Person = namedtuple('Person', 'name age _ssn', rename = True)
print(Person._fields) # Notice _ssn is replaced by _2

#%%
# You also can create a dictionary using:
    
d = djia._asdict()
print(d)
print(d['symbol'])
print(d['close'])

#%%