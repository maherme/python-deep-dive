#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:49:51 2021

@author: maherme
"""
#%%

import sys

a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a)) # It is two due to the call of getrefcount increases the reference

#%%

import ctypes


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a))) 
# In this case the result is 1 due to id(a) is evaluated and finishes before 
# to call ref_count function

#%%
# Observe how the reference counting is changing depending of how much variables
# are pointing to the same memory address:

b = a
print(id(b))
print(ref_count(id(a)))

c = a
print(ref_count(id(a)))

c = 10
print(ref_count(id(a)))

b = None
print(id(b))
print(ref_count(id(a)))

#%%
# Notice what happens here, the action to do a = None is freeing the memory
# and this memory is being using for other purposes, for this reason the
# memory address is changing.

a_id = id(a)
a = None
print(ref_count(a_id))
print(ref_count(a_id))
print(ref_count(a_id))
print(ref_count(a_id))

#%%