#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:39:54 2021

@author: maherme
"""
#%%
# Notice when value of a changes a new object is created:

a = 10
print(hex(id(a)))

a = 15
print(hex(id(a)))

a = a + 1
print(hex(id(a)))

#%%
# Notice as the both variables have the same value, are the same object:

a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))

#%%