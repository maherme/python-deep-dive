#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:08:51 2021

@author: maherme
"""
#%%

a = "hello"
b = a

print(hex(id(a)))
print(hex(id(b)))

a = "hello"
b = "hello"

print(hex(id(a)))
print(hex(id(b)))

b = "hello world"

print(hex(id(a)))
print(hex(id(b))) # Notice memory address of b changes (string is inmutable)

#%%

a = [1, 2, 3]
b = a

print(hex(id(a)))
print(hex(id(b)))

b.append(100)

print(hex(id(a)))
print(hex(id(b))) # Notice memory address is the same (list is mutable)

print(b)
print(a) # Notice changing b we have changed a (shared reference)

#%%