#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 18:03:13 2021

@author: maherme
"""
#%%

from functools import partial

def my_func(a, b, c):
    print(a, b, c)

my_func(10, 20, 30)

# We can reduce the number of arguments needed to call my_func:
def f(x, y):
    return my_func(10, x, y)

f(20, 30)

#%%

f = lambda x, y: my_func(10, x, y)
f(100, 200)

#%%

f = partial(my_func, 10)
f(20, 30)

f = partial(my_func, 10, 20)
f(30)

#%%

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

my_func(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)

def f(x, *vars, kw, **kwvars):
    return my_func(10, x, *vars, k1='a', k2=kw, **kwvars)

f(20, 100, 200, kw='b', k3=1000, k4=2000)

#%%

f = partial(my_func, 10, k1='a')
f(20, 100, 200, k2='b', k3=1000, k4=2000)

#%%

def pow(base, exponent):
    return base ** exponent

sq = partial(pow, 2) # 2 will be the base
print(sq(3))
sq= partial(pow, exponent=2) # if you want that 2 was the exponent
print(sq(3))
cu = partial(pow, exponent=3)
print(cu(5))
print(cu(base=5))
a = cu(5, exponent=2) # You can override the exponent, now it is not cubic!
print(a)

#%%

a = 2
sq = partial(pow, exponent=a)
res = sq(5)
print(res)

a = 3
res = sq(5) # It does not change, because what there is in partial is the pointed by a, the memory address.
print(res)

#%%

def my_func(a, b):
    print(a, b)

a = [1, 2]
f = partial(my_func, a)
f(100)

a.append(3) # It will change, because we are modifying the memory, this is a mutable object.
f(100)

#%%
# Let's sort some 2-D elements:

origin = (0, 0)
l = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]

dist2 = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2

result = dist2((1, 1), origin)
print(result)

f = partial(dist2, origin)
result = sorted(l, key=f)
print(result)

f = lambda x: dist2(origin, x)
result = sorted(l, key = f)
print(result)

#%%