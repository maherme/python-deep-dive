#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:34:26 2021

@author: maherme
"""
#%%
# Watch as type of variable a change depending the value stored.
# This type is the type of the object referenced by a, not the type of a.

a = "hello"
print(type(a))

a = 10
print(type(a))

a = lambda x: x**2
print(type(a))

a = 3 + 4j
print(type(a))

#%%