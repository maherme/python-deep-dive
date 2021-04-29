#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:35:40 2021

@author: maherme
"""
#%%

def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} (id={1}) was called {2} times'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    
    return inner

def add(a: int, b: int = 0):
    """
    adds two values
    """
    return a + b

print(id(add))
help(add)

add = counter(add)
print(id(add)) # Notice this add function is not the same than above
help(add)

#%%

ret = add(10, 20)
print(ret)
ret = add(20, 40)
print(ret)
ret = add(10)
print(ret)

#%%

def mult(a: int, b: int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

ret = mult(1, 2, 3, d=4)
print(ret)
ret = mult(1, 2, d=3)
print(ret)

mult = counter(mult) # Decorate mult with counter.
help(mult)

ret = mult(1, 2, 3, d=4)
print(ret)
ret = mult(1, 2, d=3)
print(ret)

#%%
# Using a decorator:

@counter
def my_func(s: str, i: int) -> str:
    return s * i

help(my_func)
ret = my_func('a', 10)
print(ret)

print(mult.__name__)
print(mult.__doc__)

#%%
# We can write some docstring for inner:

def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        """
        this is the inner closure
        """
        nonlocal count
        count += 1
        print('Function {0} (id={1}) was called {2} times'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    
    return inner

def mult(a: int, b: int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

mult = counter(mult)
help(mult)

#%%
# You can fix some documentation issues:
    
def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        """
        this is the inner closure
        """
        nonlocal count
        count += 1
        print('Function {0} (id={1}) was called {2} times'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    
    return inner

def mult(a: int, b: int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

mult = counter(mult)
help(mult)

#%%
# But the arguments are incorrect, a better way to fix this is using @wraps:

from functools import wraps

def counter(fn):
    count = 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        """
        this is the inner closure
        """
        nonlocal count
        count += 1
        print('Function {0} (id={1}) was called {2} times'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    
    # inner = wraps(fn)(inner) # This is another way to do @wraps(fn)
    return inner

def mult(a: int, b: int, c: int = 1, *, d):
    """
    multiplies four values
    """
    return a * b * c * d

help(mult)

mult = counter(mult)

help(mult)

#%%