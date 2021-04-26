#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:57:21 2021

@author: maherme
"""
#%%
# How sorted works?:

l = [1, 5, 4, 10, 9, 6]
a = sorted(l)
print(a)
print(l) # l is not changed by sorted

#%%

l = ['c', 'B', 'D', 'a']
a = sorted(l)
print(a)
print("---------------------------")
a = sorted(l, key=lambda s: s.upper()) # We can do sorted case insensitive
print(a)

#%%

d = {'def': 300, 'abc': 200, 'ghi': 100}
print(d)
for e in d:
    print(e)
a = sorted(d)
print(a)
a = sorted(d, key=lambda e: d[e]) # Now we order by value, not by key
print(a)

#%%
def dist_sq(x):
    return (x.real)**2 + (x.imag)**2

a = dist_sq(1+1j)
print(a)

l = [3+3j, 1-1j, 0, 3]
a = sorted(l, key=dist_sq) # sorted does not work with complex number, but we can use a lambda to sort them
print(a)
a = sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2)
print(a)

#%%

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Guilliam', 'Jones']
print(l)
a = sorted(l)
print(a)
a = sorted(l, key=lambda s: s[-1]) # Sorted by the last character
print(a) # If a tie exists, python keep the original order to decide what goes first

#%%

l = ['Idle', 'Cleese', 'Palin', 'Chapman', 'Guilliam', 'Jones']
print(l)
a = sorted(l, key=lambda s: s[-1])
print(a)

#%%
# Let's try to shuffle a list using lambdas and random:

import random

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l)
a = sorted(l, key=lambda x: random.random())
print(a)

#%%