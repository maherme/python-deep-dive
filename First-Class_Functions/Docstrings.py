#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 00:13:28 2021

@author: maherme
"""
#%%

def my_func(a, b=1):
    'returns a * b'
    return a * b

help(my_func)

#%%
# Comments is not the same than docstrings:

def my_func(a, b=1):
    # some comment here, this is not compile, the following is compiled:
    """returns a * b
    some additional docs here
    Inputs:
    Outputs:
    """
    return a * b

help(my_func)
print("--------------------------------")
print(my_func.__doc__)

#%%
# Annotations:

def my_func(a: 'annotation for a',
            b: 'annotation for b' = 1) -> 'something with a long annotation':
    """documentation for my_func"""
    return a * b

help(my_func)
print("--------------------------------")
print(my_func.__doc__)
print("--------------------------------")
print(my_func.__annotations__)

#%%

x = 3
y = 5
def my_func(a: 'some character', b = max(x, y)) -> 'character a repeated ' + str(max(x, y)) + ' times':
    print(b)
    return a * max(x, y)

print(my_func('a'))
print("--------------------------------")
print(my_func.__annotations__)
print("--------------------------------")
x = 10
print(my_func('a')) # Beware, b = max(x,y) is evaluated when the function is created, not when is called.
print("--------------------------------")
print(my_func.__annotations__) # The same happens with annotations

#%%

def my_func(a: str,
            b: 'int > 0' = 1,
            *args: 'some extra positional args',
            k1: 'keyword-only arg 1',
            k2: 'keyword-only arg 2' = 100,
            **kwargs: 'some extra keyword-only args') -> 'something':
    print(a, b, args, k1, k2, kwargs)

help(my_func)
print("--------------------------------")
print(my_func.__annotations__)

#%%