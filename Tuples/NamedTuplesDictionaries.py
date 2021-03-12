#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:31:03 2021

@author: maherme
"""
#%%

data_dict = dict(key1=100, key2=200, key3=300)
print(data_dict['key1'])

#%%
# Notice we can do the following because python 3.6 and above preserves the
# order of the keys and values, but it does not guarantee

from collections import namedtuple

print(data_dict.keys())
Data = namedtuple('Data', data_dict.keys())
d1 = Data(*data_dict.values())
print(d1)

#%%
# There is an important caviat with this:

d2 = Data(key1=10, key3=30, key2=20)
print(d2)
Data = namedtuple('Data', 'key3 key2 key1')
print(Data._fields)
d2 = Data(*data_dict.values())
print(d2)

#%%
# For solving this:
    
d2 = Data(**data_dict)
print(d2)

#%%

key_name = 'key2'
print(data_dict[key_name])
d2.key_name # This will fail
getattr(d2, key_name) # This will work

#%%

data_dict.get('key1', None)
data_dict.get('key10', None)
getattr(d2, 'key10') # This will fail
getattr(d2, 'key10', None) # But support default, so this will work

#%%
# Sometimes we have a list of dictionaries: 
    
data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]

#%%

keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)
print(keys)

#%%
# A better way is to use a comprehension:

keys = {key for dict_ in data_list for key in dict_.keys()}
print(keys)

#%%

Struct = namedtuple('Struct', sorted(keys))
print(Struct._fields)

#%%
# We need to create default values since each dictionary has different number
# of entries:
    
Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
Struct(key3 = 10)    

#%%
# We can create our data structure now:

tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))
print(tuple_list)

#%%
# Write a function:
    
def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', sorted(keys), rename=True)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

#%%

tuple_list = tuplify_dicts(data_list)
print(tuple_list)

#%%