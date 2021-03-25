#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:37:15 2021

@author: maherme
"""
#%%

print(type(100)) # Notice intege are classes

#%%

import sys

# This is the overhead for creating an intenger, duet to 0 does not requiere 
# memory space
print(sys.getsizeof(0))

# Notice a low value of integer needs 4 bytes:
print(sys.getsizeof(1))

# Let's see a big number:
print(sys.getsizeof(2**1000))

#%%
# Let's see if time calculation is also affected by this size:

import time

def calc(a):
    for i in range(10_000_000):
        a * 2
        
start = time.perf_counter()
calc(10)
end = time.perf_counter()
print("Small size number time:", end -start)

start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print("Big size number time:", end -start)

start = time.perf_counter()
calc(2**10_000)
end = time.perf_counter()
print("Super big size number time:", end -start)

#%%