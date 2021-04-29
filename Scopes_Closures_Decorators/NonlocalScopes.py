#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 23:43:17 2021

@author: maherme
"""
#%%

def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()

outer_func()

#%%
# This works at different levels:

def outer_func():
    x = 'hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

outer_func()

#%%

def outer_func():
    x = 'hello'
    def inner():
        x = 'python'
        print('inner:', x)
    inner()
    print('outer:', x)

outer_func()

#%%

def outer_func():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
        print('inner:', x)
    print('outer(before):', x)
    inner()
    print('outer(after):', x) # this will be x = 'python' due to is nonlocal

outer_func()

#%%
# nonlocal works with more levels:

def outer():
    x = 'hello'
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)

outer()

#%%

def outer():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        inner2()
    inner1()
    print(x)

outer()

#%%

x = 'python'

def outer():
    x = 'monty'
    def inner():
        nonlocal x
        x = 'hello'
    inner()
    print(x) # x is modified by 'hello' because is nonlocal

outer()
print(x)

#%%

x = 'python'

def outer():
    global x
    x = 'monty'
    def inner():
        global x
        x = 'hello'
    inner()
    print(x) # x is modified by 'hello' because is global, but also is modified outside the outer().

outer()
print(x)

#%%