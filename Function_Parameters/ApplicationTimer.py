#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 00:24:46 2021

@author: maherme
"""
#%%

import time

def time_it(fn, *args, **kwargs):
    print(args, kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')

#%%

def time_it(fn, *args, **kwargs):
    fn(*args, **kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***')

#%%

def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)

time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)

#%%

def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep

t = time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)
print(t)

#%%

def computer_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

c = computer_powers_1(2, end=5)
print(c)

#%%

def computer_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]

c = computer_powers_2(2, end=5)
print(c)

#%%

def computer_powers_3(n, *, start=1, end):
    # using generator expression
    return (n**i for i in range(start, end))

c = list(computer_powers_3(2, end=5)) # Notice we need to call list constructor
print(c)

#%%

t = time_it(computer_powers_1, 2, start=0, rep=5, end=20000)
print(t)
t = time_it(computer_powers_2, 2, start=0, rep=5, end=20000)
print(t)
t = time_it(computer_powers_3, 2, start=0, rep=5, end=20000)
# This is the faster because create a generator, the generator does not compute
print(t)

#%%