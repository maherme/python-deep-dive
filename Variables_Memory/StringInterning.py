#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:48:45 2021

@author: maherme
"""
#%%
# You need to do this in a console, due to in a module optimization is done
# due a compilation happens.

a = 'hello'
b = 'hello'

print(id(a), id(b))
a == b
a is b

a = 'hello world'
b = 'hello world'

print(id(a), id(b))
a == b
a is b

#%%
# We can force the interning

import sys

a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'

print(id(a), id(b), id(c))

#%%
# Let's see a difference between using is an == for comparison.

def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass
        
def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass

import time

start = time.perf_counter()
compare_using_equals(10_000_000)
end = time.perf_counter()
print('equality', end-start)

start = time.perf_counter()
compare_using_interning(10_000_000)
end = time.perf_counter()
print('equality', end-start)

# You can notice the difference in timing between equals and interning, think
# equals is comparing each character in the string and interning is comparing
# only a number, the memory address of each string.

#%%