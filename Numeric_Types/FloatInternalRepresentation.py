#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:18:51 2021

@author: maherme
"""
#%%
# Let's see the float constructor:

print(float(10))
print(float(10.4))
print(float('12.5'))
print(float('22/7')) # This will fail, you need to create a fraction first

#%%
from fractions import Fraction

a = Fraction('22/7')
print(float(a))

#%%
# Let's see the problem of the infinite number and the internal representation:

print(0.1)
print(format(0.1, '.15f'))
print(format(0.1, '.25f')) # So 0.1 is not 0.1 in the machine!

print(0.125)
print(format(0.125, '.25f')) # In this case 0.125 is stored as it is in the machine

a = 0.1 + 0.1 + 0.1
b = 0.3
print(a == b)
# Notice a is different to b in the machine!
print(format(a, '.25f'))
print(format(b, '.25f'))

#%%