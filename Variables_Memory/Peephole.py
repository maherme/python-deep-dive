#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:03:41 2021

@author: maherme
"""
#%%

def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3
    
print(my_func.__code__.co_consts) # Notice some items are precalculated

#%%
# Notice the difference in the way to store items for a list and a set

def my_func(e):
    if e in [1, 2, 3]:
        pass
    
print(my_func.__code__.co_consts) # Notice the list becomes a tuple

#%%

def my_func(e):
    if e in {1, 2, 3}:
        pass
    
print(my_func.__code__.co_consts) # Notice the set becomes a frozenset

#%%
# Let's see a performance in time about a searching in a list, a tuple and a
# set.

import string
import time

print(string.ascii_letters)

char_list = list(string.ascii_letters)
print(char_list)
char_tuple = tuple(string.ascii_letters)
print(char_tuple)
# Notice that set does not contain repeated items and does not keep the order
char_set = set(string.ascii_letters) 
print(char_set)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass
        
start = time.perf_counter()
membership_test(1_000_000, char_list)
end = time.perf_counter()
print('list', end-start)

start = time.perf_counter()
membership_test(1_000_000, char_tuple)
end = time.perf_counter()
print('tuple', end-start)

start = time.perf_counter()
membership_test(1_000_000, char_set)
end = time.perf_counter()
print('set', end-start) # Notice the set is much faster than the others

#%%