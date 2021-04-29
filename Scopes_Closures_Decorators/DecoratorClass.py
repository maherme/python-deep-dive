#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:14:04 2021

@author: maherme
"""
#%%

def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print("decorated function called a={0}, b={1}".format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def my_func(s):
    print("Hello {0}".format(s))

my_func('World')

#%%
# We can use a class callable using the __call__ method:

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        print("called a={0}, b={1}, c={2}".format(self.a, self.b, c))

obj = MyClass(10, 20)

obj.__call__(100)
obj(100) # We can do this because we are using __call__, so MyClass is callable.

#%%
# So we can use a class as a decorator in the following way:

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print("decorated function called a={0}, b={1}".format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

@MyClass(10, 20)
def my_func(s):
    print("Hello {0}".format(s))

my_func('World')

#%%

obj = MyClass(10, 20)

def my_func(s):
    print("Hello {0}".format(s))

my_func = obj(my_func)

my_func('World')

#%%