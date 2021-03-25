#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:23:49 2021

@author: maherme
"""
#%%
# bool is a subclass of int:

print(issubclass(bool, int))

# booleans are singletone object, so they kept the same memory address
print(type(True), id(True), int(True))
print(type(False), id(False), int(False))

print(id(3 < 4)) # Notice is the same memory address than above

print((3 < 4) is True)
print(None is False)

#%%
# Be careful is you don't use parenthesis:
    
print((1 == 2) == False)
print(1 == 2 == False)

#%%
# Notice python is polymorphic, and booleans are a subclass of int:
    
print(1 + True)
print(100 * False)
print((True + True + True) % 2)

#%%
# Using the constructor of bool, only 0 will result in False

print(bool(0))
print(bool(1))
print(bool(100))

#%%