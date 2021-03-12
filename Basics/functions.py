#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:36:15 2021

@author: maherme
"""
#%%
# Built in functions.

s = [1, 2, 3]

print(len(s))

#%%
# Library functions.

from math import sqrt

print(sqrt(4))

#%%

import math

print(math.pi)
print(math.exp(1))

#%%
# User defined functions.

def func_1():
    print('running func_1')
    
#%%
# This not call the function, this returns the function, is the function.

func_1

#%%
# This is a function call.

func_1()

#%%
# Use of parameters.

def func_2(a: int, b: int):
    return a * b

#%%
# The ": int" before is only information, we can pass a non integer parameter
# to the function. Notice that python is very polymorphic.

print(func_2(2, 3))
print(func_2('a', 3))
print(func_2([1, 2], 3))

#%%
# You can return a function.

def func_3():
    return func_4()

def func_4():
    return 'running func_4'

print(func_3())

#%%
# Be careful where a function is called.

def func_5():
    return func_6()

func_5()

def func_6():
    print('running func_6')
    
#%%
# You can assign function to a variable.

my_func = func_4
print(func_4())
print(my_func())

#%%
# You can also define a function as a lambda function. This is like a one line
# or an anonymous function.

fn1 = lambda x: x**2

print(fn1(2))

#%%