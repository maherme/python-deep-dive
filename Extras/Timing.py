#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:07:29 2021

@author: maherme
"""
#%%

from timeit import timeit

# This is the worse way, because we are testing import math, not only math.sqrt()
timeit(stmt='import math\nmath.sqrt(2)')
# This is the best way to do it:
timeit(stmt='math.sqrt(2)', setup='import math')
timeit(stmt='sqrt(2)', setup='from math import sqrt')

#%%
# Exists a third way to do this:
import math
timeit(stmt='math.sqrt(2)', globals=globals())

#%%

import random

l = random.choices(list('python'), k=500)
'l' in globals() # l is in globals
timeit(stmt='random.choice(l)', setup='import random', globals=globals())

#%%

def pick_random():
    randoms = random.choices(list('python'), k=500)
    return timeit(stmt='random.choice(randoms)',
                  setup='import random',
                  globals=locals())

print(pick_random())

#%%
# If we pass globals() we can referene whatever object in globals:

def pick_random(lst):
    return random.choice(lst)

print('pick_random' in globals())
print('l' in globals())

print(timeit(stmt='pick_random(l)', globals=globals()))

#%%