#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:48:03 2021

@author: maherme
"""
#%%

mod_name = 'math'
import mod_name # This will fail

#%%

import importlib
importlib.import_module(mod_name)
'math' in sys.modules
'fractions' in sys.modules
math.sqrt(2) # This will fail

#%%

'math' in globals() # Notice math is not in our namespace

# import math as math2
# math2 = sys.modules['math']
math2 = importlib.import_module(mod_name)
'math2' in globals()
id(math2)
id(sys.modules['math']) # It is the same address

math2.sqrt(2)

#%%
# To import a module you need a finder and a loader.
# You can find the loader in __spec__ attribute:

import fractions
fractions.__spec__

#%%
# finder + loader = importer
# Python has a few importers, you can find in meta_path:

sys.meta_path # When you import a module Python uses all these importers to find it.

#%%
# You can find a module using this:

importlib.util.find_spec('Decimal') # Notice Decimal is not a module, it is a class of decimal module
importlib.util.find_spec('decimal')

#%%

with open('module1.py', 'w') as code_file:
    code_file.write("print('running module1.py...')\n")
    code_file.write('a=100\n')

#%%

importlib.util.find_spec('module1')
import module1
'module1' in globals()
module1.a

#%%

import os

ext_module_path = os.environ['HOME']
file_abs_path = os.path.join(ext_module_path, 'module2.py')
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py...')\n")
    code_file.write("x = 'python'\n")

#%%

importlib.util.find_spec('module2')
sys.path
sys.path.append(ext_module_path) # With this we fix the founding of module2
importlib.util.find_spec(('module2'))

#%%

import module2
module2.x

#%%