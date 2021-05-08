#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 23:25:07 2021

@author: maherme
"""
#%%
# A module is an instance of a module class:

def func():
    a = 10
    return a

func # func is a function (type function), in the __main__ module.

globals() # This is a dictionary with the namespace, func is located here.

f = globals()['func'] # Basically namespaces are dictionaries.
f is func

#%%

locals() # This is identical to globals()
locals() is globals()

a = 100
globals() # You can see a = 100 here

def func():
    a = 10
    b = 10
    print(locals())

func() # Notice the locals here is different, has only a and b.

#%%

import math
math

junk = math
junk is math

globals()['math'] # Notice math is located in globals.
mod_math = globals()['math']
mod_math.sqrt(2)
type(globals())
type(math)
id(math)

import math
id(math) # Notice the id of math does not change when is reloaded.
# The module is instantiated in memory and referenced in globals().
# Exist a cache with the module instantiated: sys.modules

import sys
type(sys.modules) # This is the dictionary that contains the module simbols and where they are placed in memory
sys.modules['math'] # Notice math is included
id(sys.modules['math']) # The reference is the same than above

#%%
# We can do some instrospection:

math.__name__
math.__dict__ # This shows all the attributes of the math object
f = math.__dict__['sqrt']
f # f is the sqrt function.

#%%

import fractions

sys.modules['fractions']
dir(fractions)
fractions.__dict__ # Here you find the name of the module, where is placed its code ...

#%%

import types

isinstance(fractions, types.ModuleType) # Notice a module is a type ModuleType
isinstance(math, types.ModuleType)

# So we can create our own module:
#%%

mod = types.ModuleType('test', 'This is a test module.')

from types import ModuleType

isinstance(mod, ModuleType)

mod.__dict__

mod.pi = 3.14 # We can add attributes to the module
mod.__dict__
mod.pi

mod.hello = lambda: 'Hello!'
mod.hello()

hello = mod.hello # Now Hello is in globals namespace
'hello' in globals()
'mod' in globals()
hello() # This works

#%%