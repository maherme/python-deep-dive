#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:58:24 2021

@author: maherme
"""
#%%
# Dictionary ordering is guaranteed from version 3.7.

from sys import version_info
print(version_info)

#%%

d = {'b': 1, 'a':2}
d.keys(), d.values(), d.items()

d['x'] = 3
d.keys(), d.values(), d.items()

del d['a']
d.items()

d['a'] = 1
d.items() # Notice a is added to the end

#%%

d.popitem() # You can use a dictionary as stack
print(d)

#%%

d1 = {'a': 1, 'b': 200}
d2 = {'a': 100, 'd': 300, 'c': 400}

d1.update(d2)
print(d1) # Notice the merge respects the order

#%%

d = {'a': 1, 'b': 2, 'c': 3}
print('start:', d)
d['a'] = d.pop('a')
print('moved a to end:', d)

#%%
# Let's try to move a key to the start:

d = {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
print('start:', d)

d['c'] = d.pop('c')
print('moved c to end:', d)
for i in range(len(d)-1):
    key = next(iter(d.keys()))
    d[key] = d.pop(key)
print('moved c to front:', d)

#%%
# Let's pop last item:

d = {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
print('start:', d)
d.popitem()
print('pop last item:', d)

#%%
# Let's pop first item:

d = {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
print('start:', d)
key = next(iter(d.keys()))
d.pop(key)
print('after pop first item:', d)

#%%