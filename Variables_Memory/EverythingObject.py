#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:33:42 2021

@author: maherme
"""
#%%

a = 10
print(type(a)) # Notice a is a class

b = int(10) # We can create a new class using the constructor as an integer
print(b)
print(type(b))

#%%
# You can get some help using help(int) for example
# We can use the constructor according the help document:

c = int()
print(c)

c = int('101', base=2)
print(c)

#%%
# A function is also a class

def square(a):
    return a ** 2

print(type(square))

f = square

print(id(square))
print(id(f))
print(f is square)

#%%
# Notice we can return functions from other functions:

def cube(a):
    return a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube
    
f = select_function(1)

print(f is square)

f = select_function(2)

print(f is cube)

print(select_function(2)(3))

#%%

def exec_function(fn, n):
    return fn(n)

print(exec_function(cube, 3))
print(exec_function(square, 3))

#%%