#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:14:01 2021

@author: maherme
"""
#%%

import decimal
from decimal import Decimal

# Let's see // and %
# n = d*(n//d)+(n%d)

x = 10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

x = -10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

#%%

x = Decimal(10)
y = Decimal(3)
print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

x = Decimal(-10)
y = Decimal(3)
print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

#%%
# You can use some math functions looking in help(Decimal)

a = Decimal('1.5')
print(a.ln())
print(a.exp())
print(a.sqrt())

#%%
# You can also use math functions, but notice the result is different using
# math function or decimal function:

import math

x = 2
x_dec = Decimal(2)
print(format(x, '1.27f'))

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

#%%

x = 0.01
x_dec = Decimal('0.01')
print(format(x, '.27f'))

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

#%%