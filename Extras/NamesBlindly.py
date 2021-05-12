#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:29:47 2021

@author: maherme
"""
#%%
# You can and should use meaningful name for *args and **kwargs:

def audit(func):
    def inner(*args, **kwargs): # here we have no idea of what arguments are.
        print(f'Called {func.__name__}')
        return func(*args, **kwargs)
    return inner

@audit
def say_hello(name):
    return f'Hello {name}'

from operator import mul
from functools import reduce

@audit
def product(*values):
    return reduce(mul, values)

#%%

say_hello(name='Polly')
product(1, 2, 3, 4, 5)

#%%
# It has more sense call **custom_attributes than **kwargs:

class Person:
    def __init__(self, name, age, **custom_attributes):
        self.name = name
        self.age = age
        for attr_name, attr_value in custom_attributes.items():
            setattr(self, attr_name, attr_value)

parrot = Person('Polly', 101, status='stiff', vooms=False)
print(vars(parrot))

michael = Person('Palin', 42, role='shopkeeper', crooked=True)
print(vars(michael))

#%%