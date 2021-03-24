#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:56:04 2021

@author: maherme
"""
#%%
# Notice the memory address in this example of inmutable object and how this
# object does not change after the function is called.

def process(s):
    print('Initial s # = {0}'.format(id(s)))
    s = s + ' world'
    print('Final s # = {0}'.format(id(s)))
    
my_var = 'hello'
print('my_var # = {0}'.format(id(my_var)))
process(my_var)
print(my_var)

#%%
# Notice the memory address in this example of mutable object and how this
# object changes after the function is called.

def modify_list(lst):
    print('Initial lst # = {0}'.format(id(lst)))
    lst.append(100)
    print('Final lst # = {0}'.format(id(lst)))

my_list = [1, 2, 3]
print(id(my_list))

modify_list(my_list)
print(id(my_list))
print(my_list)

#%%
# Let's see with a tuple:
# Notice the inmutable element can not change, but the mutable elements inside
# an inmutable element can change.
    
def modify_tuple(t):
    print('Initial t # = {0}'.format(id(t)))
    t[0].append(100) # Assume the first element of the tuple is a list
    print('Final t # = {0}'.format(id(t)))
    
my_tuple = ([1, 2], a)
print(id(my_tuple))
modify_tuple(my_tuple)
print(my_tuple)

#%%