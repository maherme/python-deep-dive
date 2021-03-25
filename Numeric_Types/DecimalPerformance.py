#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:43:38 2021

@author: maherme
"""
#%%
# Check the memory footprint of a decimal vs a float:

from decimal import Decimal
import sys

a = 3.1415
b = Decimal('3.1415')

print(sys.getsizeof(a))
print(sys.getsizeof(b))

#%%
# Check about time performance

import time

def run_float(n=1):
    for i in range(n):
        a = 3.1415

def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')

n = 10_000_000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)

#%%

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a

def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a

n = 10_000_000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)

#%%

import math

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)

def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()

n = 5_000_000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)

#%%