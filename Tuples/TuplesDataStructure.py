#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:43:50 2021

@author: maherme
"""
#%%
# You don't need the parenthesis for creating a tuple

a = (10, 20, 30)
b = 10, 20, 30
print(type(a))
print(type(b))

#%%
# Sometimes you will need to specifi the parenthesis:
    
def print_tuple(t):
    for e in t:
        print(e)
        
print_tuple((10, 20, 30))
print_tuple(10, 20, 30) # This will fail

#%%
# We can access to a tuple indexing:

a = 'a', 10, 200

print(a[0])
print(a[1])

#%%
# We can also use slicing or iterate over a tuple

a = 1, 2, 3, 4, 5, 6
print(type(a))

print(a[2:5])

for e in a:
    print(e)
    
#%%
# We can unpack a tuple:
    
a = 'a', 10, 20

x, y, z = a
print(x)
print(y)
print(z)

#%%
# You can use extender unpacked

a = 1, 2, 3, 4, 5

x, *_, y, z = a
print(x)
print(_)
print(y)
print(z)

#%%
# Tuple is inmutable. But not the objects inside a tuple:
    
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'
    
pt = Point2D(10, 20)
print(pt)
print(id(pt))
pt.x = 100
print(pt)
print(id(pt))

#%%

a = Point2D(x=0, y=0), Point2D(10, 20)
print(a)
print(id(a[0]))
a[0].x = 100
print(a)
print(id(a[0])) # The memory address is the same than before, so is inmutable

#%%

a = 1, 2, 3
print(a)
print(id(a))

a += (4, 5)
print(a)
print(id(a)) # Notice this is a new tuple

a = a + (4, 5)
print(a)
print(id(a)) # As tuple is inmutable, adding objects to the tuple creates a new tuple

#%%

# Notice these tuples are heterogeneous
london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000

# Notice this list is homogeneous
cities = [london, new_york, beijing]

total = 0
for city in cities:
    total += city[2]
print(total)

#%%
# A better way to do the code above:
    
total = sum(city[2] for city in cities)

print(total)

#%%

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072

symbol, year, month, day, open_, high, low, close = record
print(symbol)
print(year)

symbol, *_, close = record
print(symbol, close)
print(_)

#%%
# You can unpack using a loop:

for city, country, population in cities:
    print(city, country, population)
    
#%%
# You can use enumerate:

for index, city in enumerate(cities):
    print(index, city)
    
#%%
# You can use tuple for returning several values from a function.
# This example calculates an aproximation of Pi number:

from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)
    
    if sqrt(random_x**2 + random_y**2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
        
    return random_x, random_y, is_in_circle

num_attempts = 1_000_000
count_inside = 0
for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1
        
print(f'Pi is approximately: {4 * count_inside / num_attempts}')

#%%