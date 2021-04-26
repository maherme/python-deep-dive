#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 00:49:54 2021

@author: maherme
"""
#%%

def sq(x):
    return x**2

print(type(sq))
sq # Run in the command line, notice the function name is sq(x)

#%%
# Lambda is a generic function:

lambda x: x**2 # Run in the command line, now the function name is <lambda>

#%%

lambda x, y: x+y # Run in the command line, the functio name is also <lambda>

#%%

f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(f(1, 'a', 'b', y=100, a=10, b=20))

#%%

def apply_func(x, fn):
    return fn(x)

a = apply_func(3, sq)
print(a)

#%%
# We can do the same with lambda:

a = apply_func(3, lambda x: x**2)
print(a)

#%%
# Some examples of lambda applications:

def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

a = apply_func(sq, 3)
print(a)
print("----------------------")
a = apply_func(lambda x: x**2, 3)
print(a)
print("----------------------")
a = apply_func(lambda x, y: x+y, 1, 2)
print(a)
print("----------------------")
a = apply_func(lambda x, *, y: x+y, 1, y=20)
print(a)
print("----------------------")
a = apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5)
print(a)
print("----------------------")
a = apply_func(sum, (1, 2, 3, 4, 5))
print(a)

#%%