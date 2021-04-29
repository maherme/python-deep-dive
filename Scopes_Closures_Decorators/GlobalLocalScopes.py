#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:25:14 2021

@author: maherme
"""
#%%

a = 10

def my_func(n):
    print('global a:', a)
    c = a ** n
    return c

res = my_func(2)
print(res)

#%%

def my_func(n):
    a = 20
    c = a ** n
    return c

print(a)
res = my_func(2)
print(res)
print(a) # a is not modified because a inside my_func is in other scope, is not global

#%%

def my_func(n):
    global a # Now a is global, it will change
    a = 20
    c = a ** n
    return c

print(a)
res = my_func(2)
print(res)
print(a)

#%%

def my_func():
    global var
    var = 'hello world'
    return

# print(var) # This will fail due to var is not defined
my_func()
print(var)

#%%

def my_func():
    global a
    a = 'hello'
    print('global a:', a)

my_func()
print(a)

#%%

a = 10

def my_func():
    print('global a:', a) # fails because a is local here, but is declared after using.
    a = 'hello world' # a is declared here
    print(a)

my_func()

#%%

for i in range(10):
    x = 2 * i

print(x) # Notice x exists outside the for loop.

#%%