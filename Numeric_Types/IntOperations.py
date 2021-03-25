#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 09:45:28 2021

@author: maherme
"""
#%%

print(type(1 + 1))
print(type(2 * 3))
print(type(3 ** 6))
print(type(2/3))
print(type(10/2)) # Notice this is a float also

#%%
# Let's see the floor operator included in math

import math

print(math.floor(3.999999))
print(math.floor(-3.14))
print(math.floor(-3.0000001)) # Notice this is not rounding or truncating

# Notice the difference, this is due to limited precision in float:
print(math.floor(-3.0000000000001))
print(math.floor(-3.0000000000000001))

#%%
# Notice difference between positive and negative number:

a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))

a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
print(math.trunc(a/b)) # Truncation is not the same that floor

#%%
# Notice difference between positive and negative number:

# Let's check this equation:
a = b*(a//b)+(a%b)

a = 13
b = 4

print("----- a > 0 and b > 0 -----")
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + (a%b))

a = -13
b = 4

print("----- a < 0 and b > 0 -----")
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + (a%b))

a = 13
b = -4

print("----- a > 0 and b < 0 -----")
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + (a%b))

a = -13
b = -4

print("----- a < 0 and b < 0 -----")
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + (a%b))

#%%