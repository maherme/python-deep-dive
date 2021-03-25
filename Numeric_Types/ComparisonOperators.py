#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:53:09 2021

@author: maherme
"""
#%%
# Membership operator:
    
print('a' in 'this is a test')
print(3 in [1, 2, 3])
print(3 not in [1, 2, 3])
print('key1' in {'key1': 1})
print(1 in {'key1': 1}) # This if false because is checking the keys

#%%
# Comparison operators are not supported by complex numbers:

1 + 1j < 3 + 4j

#%%
# You can mix any numeric type:

from decimal import Decimal
from fractions import Fraction

print(4 < Decimal('10.5'))
print(Fraction(2, 3) < Decimal('0.5'))
print(4 == 4 + 0j)
print(True == Fraction(2, 2))
print(True < Fraction(3, 2))

#%%
# Let's see chains of operators:

print(3 < 2 < 1/0) # Notice this works due to short-circuiting

# The next code is feasible, but probably difficult to read:
import string

print('A' < 'a' < 'z' > 'Z' in string.ascii_letters)

#%%