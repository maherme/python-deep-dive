#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 23:11:57 2021

@author: maherme
"""
#%%

i = 0

while i < 5:
    print(i)
    i += 1
    
#%%
# In python does not exist "do while" loop, but you can create as following.
# Notice that "something" will never be printed.

i = 5

while True:
    print(i)
    if i >= 5:
        break
        print('something')
        
#%%

min_length = 2
name = input("Please enter your name:")

while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name:")
    
print("Hello, {0}".format(name))

#%%
# A better way to do the code above (avoiding line repetition):
    
min_length = 2

while True:
    name = input("Please enter your name:")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
print("Hello, {0}".format(name))

#%%
# continue statement:
    
a = 0

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)
    
#%%
# else statement: look the following code
    
l = [1, 2, 3]
val = 10
found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
    
if not found:
    l.append(val)
    
print(l)

#%%
# else statement: a better way to do the code above is using else statement:

l = [1, 2, 3]
val = 10
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)
    
print(l)

#%%
# This is a try statement:

a = 10
b = 0
try:
    a/b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')
    
#%%
# Let see the try statment into a loop.
# Notice that the finally statement is executed always.
    
a = 0
b = 2

while a < 4:
    print('--------------------')
    a += 1
    b-= 1
    
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0".format(a, b))
        continue
    finally:
        print("{0}, {1} - always executes".format(a, b))
        
    print("{0}, {1} - main loop".format(a, b))
    
#%%
# Let see the try statment into a loop.
# Notice that the finally statement is executed always with break also
    
a = 0
b = 2

while a < 4:
    print('--------------------')
    a += 1
    b-= 1
    
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0".format(a, b))
        break
    finally:
        print("{0}, {1} - always executes".format(a, b))
        
    print("{0}, {1} - main loop".format(a, b))
    
#%%
# Let see the try statment into a loop.
# Notice that the else statement is only executed when the exception does not
# happen
    
a = 0
# b = 2
b = 10

while a < 4:
    print('--------------------')
    a += 1
    b-= 1
    
    try:
        a/b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0".format(a, b))
        break
    finally:
        print("{0}, {1} - always executes".format(a, b))
        
    print("{0}, {1} - main loop".format(a, b))
else:
    print('Code executed without a zero division error')
    
#%%