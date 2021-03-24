#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:08:18 2021

@author: maherme
"""
#%%

import ctypes
import gc # This is the garbage collection module

def ref_count(address):
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not Found"

# We are going to create a circular reference:
class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

# Disable garbage collector
gc.disable()

# We can check the circular reference:
my_var = A()
print(hex(id(my_var))) # This should be the same as A
print(hex(id(my_var.b))) # This should be the same as B
print(hex(id(my_var.b.a))) # This should be the same as A

#%%

a_id = id(my_var)
b_id = id(my_var.b)

print(hex(a_id))
print(hex(b_id))

print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))


#%%
# Notice that doing my_var = None the ref_count is 1, this happens because the
# garbage collector is disabled:

my_var = None

print(ref_count(a_id))
print(ref_count(b_id))

print(object_by_id(a_id))
print(object_by_id(b_id))

#%%
# Now we are going to run garbage collector:

gc.collect()

print(object_by_id(a_id))
print(object_by_id(b_id))

print(ref_count(a_id))
print(ref_count(b_id))

# If you rerun this cell several times you will watch a_id and b_id memory
# addresses are different each time, this is due to this memory has been freed.
# So you need to be very careful using memory addresses.
#%%