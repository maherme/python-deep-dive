#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 22:53:08 2021

@author: maherme
"""
#%%

def func1(a, b, *args):
    print(a)
    print(b)
    print(args)
    
func1(10, 20)
func1(10, 20, 1, 2, 3)

#%%

def avg(*args):
    count = len(args)
    total = sum(args)
    return total/count

a = avg(2, 2, 4, 4)
print(a)

#%%
# Notice this will fail:

avg()

#%%
# Let's fix this:

def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count

a = avg(2, 2, 4, 4)
print(a)
a = avg()
print(a)

#%%
# This is another way to do the function, in this way a minimum of one
# parameter is required, otherwise will fail:

def avg(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total/count

a = avg(2, 2, 4, 4)
print(a)
a = avg()
print(a)

#%%

def func1(a, b, c):
    print(a)
    print(b)
    print(c)

l = [10, 20, 30]
func1(*l) # if you do func1(l), this will fail because you are passing only 1 parameter

#%%
# If you can support whatever size of the list, with a minimum value:

def func1(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)

l = [10, 20, 30, 40, 50]
func1(*l)

#%%