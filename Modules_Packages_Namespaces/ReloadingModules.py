#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 23:43:50 2021

@author: maherme
"""
#%%
# Note: you need to do this in a jupiter notebook or in a terminal.

# Let's write a function to create a module:
    
import os

def create_module_file(module_name, **kwargs):
    '''Create a module file named <module_name>.py
    Module has a single function (print_values) that will print
    out the supplied (stringfied) kwargs.
    '''
    
    module_file_name = f'{module_name}.py'
    # module_file_name = '{0}.py'.format(module_name)
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)
    
    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")
            
#%%

create_module_file('test', k1=10, k2='python')

#%%

import test
test
test.print_values()

#%%
# Let's change the module:

create_module_file('test', k1=10, k2='python', k3='cheese')

#%%

import test # Notice nothing happens now, the module is not reimported
test.print_values() # The value 'cheese' is not printed
import sys
'test' in sys.modules # Test is in sys.modules, for that reason Python did not import it
id(test)

#%%
# We can delete and import the module again:
del sys.modules['test']
import test
id(test), id(sys.modules['test']) # Notice the id is different than before, this is a new object
test.print_values()

# But if any module imported test before, this module will stop to work ...

#%%
# We can think in using reload to fix this problem:

create_module_file('test', k1=10, k2='python', k3='cheese', k4='parrots')

import importlib

importlib.reload(test) # Notice the module is reloaded now, the memory address has not changed
test.print_values()
id(test), id(sys.modules['test'])

#%%
# Take into account that reimport a module is not safe:

create_module_file('test2', k1='python')

from test2 import print_values

'test2' in globals() # We don't have test2 in globals namespace.
'test2' in sys.modules # We have the reference of test2 in the dictionary.
print_values
print_values()

create_module_file('test2', k1='python', k2='cheese')

importlib.reload(sys.modules['test2'])
# Notice the print_values() has not been updated, the print_values is in globals.
# We have udpated the test2 object, but the reference of print_values is pointing to the older test2 version imported before.
print_values() 

# To fix the issue we can do "from test2 import print_values" again or:
print_values = sys.modules['test2'].print_values
print_values()
