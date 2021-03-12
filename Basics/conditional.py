#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:18:09 2021

@author: maherme
"""
#%%
# Basic.

a = 6

if a < 5:
    print('a < 5')
else:
    print('a  >= 5')
    
#%%
# Nested.

a = 5

if a < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a < 10')
    else:
        print('a >= 10')
        
#%%
# Branching.

a = 25

if a < 5:
    print('a < 5')
elif a < 10:
    print('5 <= a < 10')
elif a < 15:
    print('10 <= a < 15')
elif a < 20:
    print('15 <= a < 20')
else:
    print('a > 20')
    
#%%
# Conditional expresion: X if (condition is true) else Y
# It is not used to manage blocks of code.

a = 25

b = 'a < 5' if a < 5 else 'a >= 5'

print(b)

#%%
# The above code is the same as:
    
a = 25

if a < 5:
    b = 'a < 5'
else:
    b= 'a >= 5'
    
print(b)

#%%