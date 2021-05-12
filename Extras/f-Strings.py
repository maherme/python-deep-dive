#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:19:58 2021

@author: maherme
"""
#%%
# Python 3.6 introduces f-Strings.
# f-Strings is short for formatted string literals.

from sys import version_info
print(version_info)

#%%
# Three ways to do the same:

'{} % {} = {}'.format(10, 3, 10 % 3)

'{1} % {2} = {0}'.format(10 % 3, 10, 3)

'{a} % {b} = {mod}'.format(a=10, mod=10 % 3, b=3)

#%%
# You can use f'':

a = 10
b = 3
f'{a} % {b} = {a % b}'

a = 10/3
f'{a:0.5f}'

f'{10/3:0.5f}'

name = 'Python'
f'{name} rocks!'

#%%

def outer():
    name = 'Python'
    
    def inner():
        return f'{name} rocks!'
    
    return inner

print(outer()())

#%%

sq = lambda x: x**2
a = 10
b = 1
print(f'{sq(a) if b > 5 else a}')
b = 10
print(f'{sq(a) if b > 5 else a}')
a = 10
b = 1
print(f'{(lambda x: x**2)(a) if b > 5 else a}')
b = 10
print(f'{(lambda x: x**2)(a) if b > 5 else a}')

#%%
