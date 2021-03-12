#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:43:32 2021

@author: maherme
"""
#%%
# In Python, an iterable is an object capable of returning values one at a
# time.
# In other lenguages a for loop is similar to: for(int i=0; i<5; i++){...}
# This is similar to a while loop:
    
i = 0
while i < 5:
    print(i)
    i += 1
i = None

#%%
# In Python a for loop is used with iterable items.
# In this code range() is an iterable which return a number which is stored in
# i.

for i in range(5):
    print(i)
    
#%%
# As iterable, you can do a for with a list:
    
for i in [1, 2, 3, 4]:
    print(i)
    
#%%
# You can also use a string:
    
for c in 'hello':
    print(c)
    
#%%
# You can also use a tuple:
    
for x in ('a', 'b', 'c', 4):
    print(x)
    
#%%
# You can create more complex loops:

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)
    
#%%
# You can use other statements inside a for loop:
    
for i in range(5):
    if i == 3:
        break
    print(i)
    
#%%
# You can also use an "else" statement:

for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('no multiples of 7 in the range')
    
#%%
# You can also use "try catch" statement. This working in the same way than
# in while loop.

for i in range(5):
    print('--------------------')
    try:
        10/(i-3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always run')
        
    print(i)
        
#%%
# You don't need the index for an iterable with index like a string:

s = 'hello'
for c in s:
    print(c)
    
#%%

s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1
    
#%%

s = 'hello'

for i in range(len(s)):
    print(i, s[i])
    
#%%
# This is a more readable way to implement the code above:

s = 'hello'

for i, c in enumerate(s):
    print(i, c)
    
#%%