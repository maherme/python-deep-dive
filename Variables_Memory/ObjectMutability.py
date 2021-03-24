#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:43:33 2021

@author: maherme
"""
#%%
# Notice the object my_list is the same when we append a new item

my_list = [1, 2, 3]
print(id(my_list))

my_list.append(4)
print(id(my_list))

#%%
# Notice the object my_list_1 is a different object when the add a new item

my_list_1 = [1, 2, 3]
print(id(my_list_1))

my_list_1 = my_list_1 + [4]
print(id(my_list_1))

#%%
# Notice the object my_dict is the same when we add a new item

my_dict = dict(key1=1, key2='a')
print(id(my_dict))

my_dict['key3'] = 10.5
print(id(my_dict))

#%%
# Notice tuple is inmutable, but the inside element in the tuple can be mutable

t = (1, 2, 3)
print(id(t))
print(id(t[0]))
print(id(t[1]))

# Let's create a tuple which contains lists
t = ([1, 2], [3, 4])
print(id(t)) # Notice id of t has changed

t[0].append(3)
print(t)
print(id(t)) # Notice id of t has not changed using append method

#%%