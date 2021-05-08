#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 00:14:41 2021

@author: maherme
"""
#%%

import sys

for key in sorted(sys.modules.keys()):
    print(key)

'cmath' in sys.modules
'cmath' in globals()

#%%

from cmath import exp

'cmath' in globals() # Notice cmath is not in globals
'exp' in globals()
exp
id(exp)
'cmath' in sys.modules
exp(2+2j) # We can call exp, but not cmath.exp()

#%%

cmath = sys.modules['cmath']
'cmath' in globals() # Now cmath is in globals
cmath.exp(2+2j) # We can call cmath methods

#%%
# Notice a problem with import * :

from cmath import *

globals() # Notice all cmath libraries all included now in globals

sin(2+2j) # This will work

from math import *

globals() # Notice some cmath libraries have been overwritten by math libraries

sin(2+2j) # Notice this fails, because is using math library and not cmath

#%%
# You can do:

from cmath import sin as c_sin
from math import sin as r_sin

#%%

from time import perf_counter
from collections import namedtuple

Timings = namedtuple('Timings', 'timing_1 timing_2, abs_diff rel_diff_perc')

def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1)/timing1 * 100
    
    timings = Timings(round(timing1, 1),
                      round(timing2, 1),
                      round(timing2 - timing1, 1),
                      round(rel_diff, 2))
    return timings

#%%

test_repeats = 10_000_000

#%%
# Timing using fully qualified module.symbol

import math

start = perf_counter()
for _ in range(test_repeats):
    math.sqrt(2)
end = perf_counter()
elapsed_fully_qualified = end - start
print(f'Elapsed: {elapsed_fully_qualified}')

#%%
# Timing using a directly import symbol name

from math import sqrt

start = perf_counter()
for _ in range(test_repeats):
    sqrt(2)
end = perf_counter()
elapsed_direct_symbol = end - start
print(f'Elapsed: {elapsed_direct_symbol}')

#%%

compare_timings(elapsed_fully_qualified, elapsed_direct_symbol)

#%%
# Timing using a function wrapper (fully qualified symbol)

import math

def func():
    math.sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_fully_qualified = end -start
print(f'Elapsed: {elapsed_func_fully_qualified}')

#%%

from math import sqrt

def func():
    sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_direct_qualified = end -start
print(f'Elapsed: {elapsed_func_direct_qualified}')

#%%

compare_timings(elapsed_func_fully_qualified, elapsed_func_direct_qualified)

#%%
# Nested imports

def func():
    import math
    math.sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_fully_qualified = end -start
print(f'Elapsed: {elapsed_nested_fully_qualified}')

#%%

compare_timings(elapsed_func_fully_qualified, elapsed_nested_fully_qualified)

#%%
# Notice this is much slower, because it needs to look up where sqrt is placed,
# and also replace sqrt in local namespaces every time func is called.

def func():
    from math import sqrt
    sqrt(2)

start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_direct_symbol = end - start
print(f'Elapsed: {elapsed_nested_direct_symbol}')

#%%

compare_timings(elapsed_nested_fully_qualified, elapsed_nested_direct_symbol)

#%%