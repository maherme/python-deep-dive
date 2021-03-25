#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:01:19 2021

@author: maherme
"""
#%%
# Let's see trunc function:

from math import trunc

print(trunc(10.3), trunc(10.5), trunc(10.9))

# Trunc is used by default for the int constructor:
print(int(10.4), int(10.5), int(10.9))

#%%
# Let's see floor function:

from math import floor

print(floor(10.3), floor(10.5), floor(10.9))
# Notice the difference between floor and trunc is in negative numbers:
print(trunc(10.4), trunc(10.5), trunc(10.9))
print(floor(-10.4), floor(-10.5), floor(-10.9))

#%%
# Let's see ceil function:

from math import ceil

print(ceil(10.4), ceil(10.5), ceil(10.9))
print(ceil(-10.4), ceil(-10.5), ceil(-10.9)) # Notice -10 is greater than -11

#%%