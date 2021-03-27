#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:26:59 2021

@author: maherme
"""
#%%

from datetime import datetime

d = datetime.utcnow()
print(d)

#%%

def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))

log('message 1', dt='2001-01-01 00:00:00.000')
log('message 2')

#%%
# Notice de date does not change, because the method utcnow was executed only
# once above:
log('message 3')

#%%

def log(msg, *, dt=None):
    if not dt:
        dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

log('message 1', dt='2010-01-01')
log('message 2')

#%%
# Using short-circuiting:

def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

log('message 1', dt='2010-01-01')
log('message 2', dt=None)
log('message 3')

#%%

my_list = [1, 2, 3]

def func(a=my_list):
    print(a)

func()
func(['a', 'b'])
my_list.append(4)
func() # Notice the default value has changed

#%%
# A solution is using a tuple:
    
my_list = (1, 2, 3)

def func(a=my_list):
    print(a)

func()
func(['a', 'b'])
my_list.append(4) # This will fail
func() # Notice the default value has changed

#%%

def add_item(name, quantity, unit, grocery_list):
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list

store1 = []
store2 = []

add_item('banana', 2, 'units', store1)
add_item('milk', 1, 'liter', store1)
print(store1)

add_item('python', 1, 'medium-rare', store2)
print(store2)

#%%

del store1
del store2

#%%

def add_item(name, quantity, unit, grocery_list=[]):
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list

store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'liter', store1)

print(store1)

store2 = add_item('python', 1, 'medium-rare')

print(store2)
print(store1)
# Notice both store are the same object, this happens because we are using the
# default objetc grocery_list=[], and this is created only once
# Be careful when working with mutable object as default parameter
print(store1 is store2)

#%%
# To fix the issue above:

def add_item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append("{0} ({1} {2})".format(name, quantity, unit))
    return grocery_list

store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'liter', store1)

print(store1)

store2 = add_item('python', 1, 'medium-rare')

print(store2)

print(store1 is store2)

#%%

def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n-1)

factorial(3)
factorial(3) # Notice it is needed to recalculate everything

#%%

def factorial(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n-1, cache=cache)
        cache[n] = result
        return result

cache = {}
factorial(3, cache=cache)
print(cache)
factorial(4, cache=cache)

#%%
# In this case a mutable default parameter could improve the usage of the
# function:

def factorial(n, *, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n-1)
        cache[n] = result
        return result

factorial(3)
factorial(3)
factorial(4)

#%%