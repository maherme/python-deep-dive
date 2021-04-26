#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:42:57 2021

@author: maherme
"""
#%%

def my_func(a: "mandatory positional",
            b: "optional positional" =1, 
            c=2, 
            *args: "add extra positional here", 
            kw1, 
            kw2=100, 
            kw3=200, 
            **kwargs: "provide extra kw-only here") -> "dones nothing":
    """This function does nothing but does have various parameters
    and annotations.
    """
    i = 10
    j = 20

print(my_func.__doc__)
print("-----------------------------------------")
print(my_func.__annotations__)
print("-----------------------------------------")
my_func.short_description = "this is a function that does nothing much"
print(my_func.short_description)

#%%

dir(my_func) # Run this in the command line and this shows all the attributes.

#%%

print(my_func.__name__)
a = id(my_func)
print(a)

#%%

def func_call(f):
    print(id(f))
    print(f.__name__)

func_call(my_func)

#%%

print(my_func.__defaults__) # This shows the default parameters
print(my_func.__kwdefaults__) # This shows the default keyword parameters

#%%

print(my_func.__code__)
print("-----------------------------------------")
dir(my_func.__code__) # code is an object so we can watch its attributes
print(my_func.__code__.co_name)
print("-----------------------------------------")
print(my_func.__code__.co_varnames)
print("-----------------------------------------")
print(my_func.__code__.co_argcount) # This shows only positional arguments

#%%
# It is easier use the inspect module:

import inspect
from inspect import isfunction, ismethod, isroutine

a = 10
print(isfunction(a))
print(isfunction(my_func))
print(ismethod(my_func))

#%%

class MyClass:
    def f(self):
        pass

print(isfunction(MyClass.f))
my_obj = MyClass()
print(isfunction(my_obj.f))
print(ismethod(my_obj.f))
print(isroutine(my_obj.f))
print(isroutine(MyClass.f))

#%%

# TODO: Fix this function
# currently does nothing, but should do ...
def my_func(a: "mandatory positional",
            b: "optional positional" =1, 
            c=2, 
            *args: "add extra positional here", 
            kw1, 
            kw2=100, 
            kw3=200, 
            **kwargs: "provide extra kw-only here") -> "dones nothing":
    """This function does nothing but does have various parameters
    and annotations.
    """
    i = 10
    j = 20
    a = i + j
    return a

print(inspect.getsource(my_func))
print("-----------------------------------------")
print(inspect.getmodule(my_func))
print("-----------------------------------------")
print(inspect.getcomments(my_func))

#%%

print(inspect.signature(my_func))
print("-----------------------------------------")
dir(inspect.signature(my_func)) # Run in the command line
print("-----------------------------------------")
print(my_func.__annotations__)
print("-----------------------------------------")
print(inspect.signature(my_func).return_annotation)

#%%

sig = inspect.signature(my_func)
print(sig.parameters)

#%%

for k, v in sig.parameters.items():
    print(dir(v))

#%%

for k, param in sig.parameters.items():
    print('Key:', k)
    print('Name:', param.name)
    print('Default:', param.default)
    print('Annotation:', param.annotation)
    print('Kind:', param.kind)
    print("-----------------------------------------")

#%%

help(divmod) # Notice the / character, it means the parameters are positional only:

for param in inspect.signature(divmod).parameters.values():
    print(param.kind)

#%%