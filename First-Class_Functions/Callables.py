#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 22:36:12 2021

@author: maherme
"""
#%%

a = callable(print)
print(a)

# All callables return a value:
result = print("hello")
print(result)

#%%

l = [1, 2, 3]
a = callable(l.append)
print(a)
result = l.append(4)
print(l)
print(result)

#%%

s = 'abc'
result = callable(s.upper) # Notice is s.upper and not s.upper()
print(result)
result = s.upper()
print(result)

#%%

from decimal import Decimal

result = callable(Decimal)
print(result)
a = Decimal('10.5')
print(type(a))
result = callable(a)
print(result)

#%%

class MyClass:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x

result = callable(MyClass)
print(result)

a = MyClass(100)
a.counter
result = callable(a)
print(result)

#%%

class MyClass:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x
        
    def __call__(self, x=1):
        print('updating counter...')
        self.counter += x
    
b = MyClass()
MyClass.__call__(b, 10)
print(b.counter)
result = callable(b)
print(result)
b()
print(b.counter)
b(100)
print(b.counter)

#%%