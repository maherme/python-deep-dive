#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:19:57 2021

@author: maherme
"""
#%%

def my_func(a, b, c):
    print("a = {0}, b = {1}, c = {2}".format(a, b, c))

my_func(1, 2, 3)

#%%
# This will fail:

my_func(1, 2)

#%%
# We can define default argument values (keywords) to avoid the failure above:

def my_func(a, b=2, c=3):
    print("a = {0}, b = {1}, c = {2}".format(a, b, c))

my_func(10, 20, 30)
my_func(10, 20)
my_func(10)

#%%
# You can call the function with the argument urordered:

my_func(c=30, b=20, a=10)
my_func(10, c=30, b=20)
my_func(10, c=30)

#%%