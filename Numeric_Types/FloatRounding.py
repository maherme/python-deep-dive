#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:15:14 2021

@author: maherme
"""
#%%
# Round function is built-in in python.

a = round(1.9)
print(a, type(a)) # Notice round is casting to int also

a = round(1.9, 0)
print(a, type(a)) # Notice round is keepting the type of a

#%%
# Let's see how the parameter of round works:

print(round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888,0))
# Notice the behaviour for negative:
print(round(888.88, 1), round(888.88, 0), round(888.88, -1), round(888.88, -2), 
      round(888.88, -3), round(888.88, -4))
# Notice for the last one than 0 is closer than 10000 to 888.88

#%%
# Let's see the ties:

# Notice the bank rounding, always round to the closest even number
print(round(1.25, 1), round(1.35, 1))
print(round(-1.25, 1), round(-1.35, 1))

#%%

def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))

print(round(1.5), _round(1.5))
print(round(2.5), _round(2.5))
print(round(-1.5), _round(-1.5))
print(round(-2.5), _round(-2.5))

#%%