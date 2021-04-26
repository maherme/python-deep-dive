#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:10:00 2021

@author: maherme
"""
#%%

l = [5, 8, 6, 10, 9]
_max = lambda x, y: x if x > y else y
result = _max(3, 4)
print(result)

#%%

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

result = max_sequence(l)
print(result)

#%%

_min = lambda a, b: a if a < b else b
result = _min(3, 4)
print(result)

#%%

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result

result = min_sequence(l)
print(result)

#%%

_add = lambda a, b: a + b
result = _add(1, 2)
print(result)

#%%

def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result

result = add_sequence(l)
print(result)

#%%
# Doing the function more generic:

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

result = _reduce(_max, l)
print(result)
result = _reduce(_min, l)
print(result)
result = _reduce(_add, l)
print(result)

#%%
# Notice this will fail due to set is not indexable, is not a sequence

result = _reduce(_max, {1, 3, 4, 5})

#%%
# We can use reduce function from functools:

from functools import reduce

result = reduce(_max, l)
print(result)
result = reduce(_add, l)
print(result)
result = reduce(_max, {1, 3, 4, 5}) # Now set will work. Python uses a different technique.
print(result)

#%%

s = {True, 1, 0, None}
result = all(s) # all do an "and" between all the elements
print(result)
result = bool(True) and bool(1) and bool(0) and bool(None)
print(result)

#%%

s2 = {True, 1, "s"}
result = all(s2)
print(result)
result = bool(True) and bool(1) and bool('s')
print(result)

#%%

result = any(s) # any is similar to all, but do an "or" instead.
print(result)
result = any(s2)
print(result)

#%%

s3 = {False, 0, '', None}
result = any(s3)
print(result)

#%%
# Let's do all and any using reduce and lambda:

result = reduce(lambda a, b: bool(a) and bool(b), s)
print(result)

result = reduce(lambda a, b: bool(a) or bool(b), s3)
print(result)

#%%

l = [1, 2, 3, 4]
result = reduce(lambda a, b: a * b, l)
print(result) # We calculate a factorial using a reduce function

#%%
# n! = 1*2*3* ... *n

result = reduce(lambda a, b: a * b, range(1, 5+1))
print(result)

#%%

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

result = fact(5)
print(result)

#%%

def fact(n):
    return reduce(lambda a, b: a * b, range(1, n+1))

result = fact(5)
print(result)

#%%
# Now we will not use index:

def _reduce(fn, sequence, initial):
    result = initial
    for x in sequence:
        result = fn(result, x)
    return result

l = [1, 2, 3, 4]
result = _reduce(lambda a, b: a + b, l, 0)
print(result)
result = _reduce(lambda a, b: a + b, l, 100)
print(result)

#%%
# And reduce function from functools works in the same way:

result = reduce(lambda a, b: a + b, {1, 2, 3, 4}, 0)
print(result)
result = reduce(lambda a, b: a + b, {1, 2, 3, 4}, 100)
print(result)

#%%