#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:44:29 2021

@author: maherme
"""
#%%

from fractions import Fraction

# You can get some help typing help(Fraction) in the python console
# There are many ways to create a fraction number:
    
print(Fraction(1))
print(Fraction(denominator=1, numerator=2))
print(Fraction(2, 1))
print(Fraction(numerator=1, denominator=2))
print(Fraction(1, 2))
print(Fraction(0.125))
print(Fraction('0.125'))
print(Fraction(22/7))

#%%
# All arithmetic operators work:

x = Fraction(2, 3)
y = Fraction(3, 4)

print(x + y)
print(x * y)
print(x/y)

#%%
# Python simplify the fractions also:

print(Fraction(8, 16))

#%%
# The sign of a fraction is set in the numerator:

print(Fraction(1, -4))
x = Fraction(1, -4)
print(x.numerator)
print(x. denominator)

#%%
# Let's see precision in rational vs floats:

import math

x = Fraction(math.pi)
print(x)
print(float(x))

y = Fraction(math.sqrt(2))
print(y)
print(float(y))

#%%

a = 0.125
print(a)

b = 0.3
print(b)

print(Fraction(a))
print(Fraction(b)) # Notice the representation of 0.3

#%%
# Let's see 0.3 in more detail:

print(format(b, '0.5f'))
print(format(b, '0.15f'))
print(format(b, '0.25f')) # So 0.3 is not stored as 0.3 in the machine!

#%%
# We can limit the denominator value in the aproximation of the fraction:

x = Fraction(0.3)
print(x.limit_denominator(10))

#%%
# Let's see with pi number

x = Fraction(math.pi)
print(x)
print(float(x))
print(x.limit_denominator(10))
print(22/7)
print(x.limit_denominator(100))
print(x.limit_denominator(100_000))
print(312689/99532)

#%%