#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:28:24 2021

@author: maherme
"""
#%%
# Remember:

x = 0.1
print(x)
print(format(x, '.25f'))

x = 0.125
print(x)
print(format(x, '.25f'))

x = 0.125 + 0.125 + 0.125
y = 0.375
print(x == y) # This is true because x and y have exact representation

x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y) # This is false because x and y have not finite representation

#%%
# So, how compare floats:

# We can round:
print(round(x, 3) == round(y, 3))

# But this method has a problem with absolute and relative tolerances:

x = 10000.01
y = 10000.02
print(y/x)
print(round(x, 1) == round(y, 1))

x = 0.01
y = 0.02
print(y/x)
print(round(x, 1) == round(y, 1)) # This is true but x and y are quite different

#%%
# For the reason above is preferable to use the isclose method:

from math import isclose

x = 0.1 + 0.1 + 0.1
y = 0.3
print(isclose(x, y))
print(x == y)

#%%
# You can face problems using only relative tolerance with small numbers:

x = 123456789.01
y = 123456789.02
print(isclose(x, y, rel_tol=0.01))

x = 0.01
y = 0.02
print(isclose(x, y, rel_tol=0.01))

x = 0.0000001
y = 0.0000002
print(isclose(x, y, rel_tol=0.01))

#%%
# To fix the problem above you need to use absolute tolerance:

print(isclose(x, y, rel_tol=0.01, abs_tol=0.01))

x = 0.0000001
y = 0.0000002
a = 123456789.01
b = 123456789.02

# Normally you will use the same value of abs_tol and rel_tol during the
# execution of your program, so you should choose a value which works fine:
print(isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print(isclose(a, b, abs_tol=0.0001, rel_tol=0.01))

#%%