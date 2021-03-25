#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:36:03 2021

@author: maherme
"""
#%%
# The constructor of bool is really calling __bool__ method when a number is
# passed:

print(bool(100), (100).__bool__())
print(bool(0), (0).__bool__())

# In the case of a list the method called is __len__ :
a = []
print(bool(a), bool(a.__len__()))

#%%
# Let's see numerical types:

from decimal import Decimal
from fractions import Fraction

print(bool(Fraction(0, 1)), bool(Decimal('0.0')))
print(bool(10.5), bool(1j), bool(Fraction(1, 2)), bool(Decimal('10.5')))

#%%
# Let's see sequence types:

a = [1, 2]
b = 'abc'
c = (1, 2)

print(bool(a), bool(b), bool(c))

#%%
# Let's see map types:

a = {'a' : 1}
b = {1, 2}

print(bool(a), bool(b))

#%%

a = [1, 2, 3]

if a is not None and len(a) > 0:
    print(a[0])
else:
    print('Nothing to see here...')

#%%
# This code works in the same way than the above

a = None

if a:
    print(a[0])
else:
    print('Nothing to see here...')

#%%