#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:21:35 2021

@author: maherme
"""
#%%
# Let's do a recursive fibonacci implementation:

def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(10) # Notice this is quite inefficient

#%%
# Let's improve this using a cache:

class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}
        
    def fib(self, n):
        if n not in self.cache:
            print('Calculating fib({0})'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

f = Fib()
f.fib(10) # Notice now less calculation is needed

#%%
# Let's do this using a closure:

def fib():
    cache = {1: 1, 2: 1}
    
    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    
    return calc_fib

f = fib()
f(10)
g = fib()
g(10) # Notice g and f don't share the cache.

#%%
# Let's do it using a decorator:

def memoize_fib(fib):
    cache = {1: 1, 2: 1}
    
    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]
    
    return inner

@memoize_fib
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(10)

#%%
# We can do the decorator more generic:

def memoize(fn):
    cache = dict()
    
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    
    return inner

@memoize
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(10)
print("----------")
fib(10)
print("----------")
fib(11)

#%%

@memoize
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)

fact(6)
print("----------")
fact(6)
print("----------")
fact(7)

#%%

@memoize
def fib(n):
    return 1 if n < 3 else fib(n-1) + fib(n-2)

from time import perf_counter

start = perf_counter()
print(fib(200))
end = perf_counter()
print(end -start)

#%%
# Really, for the cache purpose Python has a decorator already built in:

from functools import lru_cache

@lru_cache()
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(10)
print("----------")
fib(11)

#%%
# We can limit the size of the cache:

@lru_cache(maxsize=8)
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(8)
print("----------")
fib(8)
print("----------")
fib(16)
print("----------")
fib(8)
print("----------")
fib(9)

#%%