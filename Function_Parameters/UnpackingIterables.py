#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:27:59 2021

@author: maherme
"""
#%%

a, b, c = [1, 'a', 3.14] # Positional unpacking
print(a, b, c)

(a, b) = (1, 2)
print(a, b)

a, b = 10, 20 # This is sometimes called parallel assigment
print(a, b)

a, b, c = 10, {1, 2}, ['a', 'b'] # Unpacking suport different types
print(a, b, c)

#%%
# The following code works because python evaluates the right side and assign
# the variables to a memory address before to evaluate the left side

a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

#%%
# You can unpack whatever iterable:

for e in 'XYZ':
    print(e)

a, b, c = 'XYZ'
print(a, b, c)

#%%
# Be careful with unordered types:

s = {'h', 'p', 't', 'o', 'n', 'y'}

for e in s:
    print(e)

#%%

d = {'a':1, 'b':2, 'c':3}

for e in d:
    print(e)

#%%

# Notice here d finally will point to 4, not to the dictionary
# Remember: python evaluates completely the right side before the left
d = {'a':1, 'b':2, 'c':3, 'd':4}
a, b, c, d = d
print(a, b, c, d)

#%%
# If you want to iterate the values and not the keys you can use the values()
# method

d = {'a':1, 'b':2, 'c':3, 'd':4}
for e in d.values():
    print(e)

#%%
# If you want to unpack both, keys and values, you can use the items() method

d = {'a':1, 'b':2, 'c':3, 'd':4}
for a, b in d.items():
    print('key={0}, value={1}'.format(a, b))

#%%