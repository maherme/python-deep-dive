#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 23:13:48 2021

@author: maherme
"""
#%%

def func1(a, b, *args, d):
    print(a, b, args, d)

func1(1, 2, 3, 4, 5) # This will fail due to args run out the parameters

#%%
# You need to use keyword:

func1(1, 2, 3, 4, d=5)

#%%
# the * set the last positional parameter:

def func(*, d):
    print(d)

func(d=100)
func(1, 2, d=100) # This will fail

#%%

def func(a, b, *, d):
    print(a, b, d)

func(1, 2, d=4)

#%%

def func(a, b=2, *args, d):
    print(a, b, args, d)

func(1, 5, 3, 4, d='a')

#%%

def func(a, b=20, *args, d=0, e):
    print(a, b, args, d, e)

func(5, 4, 3, 2, 1, e='hello') # d is not mandatory
func(0, 600, d='hello', e='python')
func(11, 'm/s', 24, 'mph', d='unladen', e='swallow')

#%%

def func(**others):
    print(others)

func(a=1, b=2, c=3)

#%%

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, x=100, y=200)

#%%

def func(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)

func(1, 2, x=100, y=200, d=20)

#%%

def func(a, b, **kwargs):
    print(a)
    print(b)
    print(kwargs)

func(1, 2, x=100, y=200)

#%%