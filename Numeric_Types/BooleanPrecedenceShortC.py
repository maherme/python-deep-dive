#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:18:38 2021

@author: maherme
"""
#%%
# Precedence is: not --> and --> or

print(True or True and False)
print(True or (True and False))
print((True or True) and False) # This is different due to precedence

#%%
# Short-Circuiting:
# True or Y --> True, whatever Y was
# False and Y --> False, whatever Y was

a = 10
b = 2

if a/b > 2:
    print('a is at least twice b')

#%%
# This code will fail:

a = 10
b = 0

if a/b > 2:
    print('a is at least twice b')

#%%
# We can fix the problem above using short-circuiting:

a = 10
b = 0

if b > 0 and a/b > 2:
    print('a is at least twice b')

#%%
# We can use even a better syntax:

a = 10
b = 0

if b and a/b > 2: # If b = None, in this case will not fail
    print('a is at least twice b')

#%%

import string

name = 'Bob'
if name[0] in string.digits:
    print("Name cannot start with a digit.")

#%%
# The code above will fail if name is empty, let's fix that:

name = ''
# if name is not None and len(name) > 0 and name[0] in string.digits:
if name and name[0] in string.digits: # This syntax is equivalent to the commented above
    print("Name cannot start with a digit.")
    
#%%