#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:19:38 2021

@author: maherme
"""
#%%
# Notice the difference between == and is depending of the memory address:

a = 10
b = 10

print(id(a))
print(id(b))

print("a is b", a is b)
print("a == b", a == b)

#%%

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print("a is b", a is b)
print("a == b", a == b)

#%%

a = 10
b = 10.0

print("a is b", a is b)
print("a == b", a == b)

#%%
# Notice about None is an object

print(id(None))
print(type(None))

a = None
b = None
c = None

print(a is b)
print(a is c)
print(a is None)
print(b is None)
print(c is None)

#%%