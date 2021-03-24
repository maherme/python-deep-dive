#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:35:10 2021

@author: maherme
"""
#%%
# Python uses integer optimization in a range [-5, 256].
# You need to do this in a console, due to in a module optimization is done
# due a compilation happens.
# In a console you will see a is b is False.

a = 10
b = 10

print(id(a))
print(id(b))
a is b

a = -5
b = -5

print(id(a))
print(id(b))
a is b

a = 256
b = 256

print(id(a))
print(id(b))
a is b


a = 257
b = 257

print(id(a))
print(id(b))
a is b

#%%

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)

print(id(a), id(b), id(c), id(d))

#%%