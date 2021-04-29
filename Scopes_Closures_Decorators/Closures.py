#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:23:43 2021

@author: maherme
"""
#%%

def outer():
    x = 'python'
    
    def inner():
        print(x) # x is a nonlocal variable, so inner and x forms a closure
        
    return inner

fn = outer()
print(fn.__code__.co_freevars) # x is a free variable
print(fn.__closure__)

#%%

def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    
    def inner():
        x = [1, 2, 3] # x is local variable, it is not a free variable
        print(hex(id(x)))
        
    return inner

fn = outer()
fn() # Notice x in inner has a different memory address

#%%
# If the variable is referenced:

def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    
    def inner():
        y = x
        print(hex(id(y)))
        
    return inner

fn = outer()
print(fn.__closure__)
fn() # Notice y is pointing to the same label than x

#%%
# Write a closure for modifying the closure:

def outer():
    count = 0
    
    def inc():
        nonlocal count
        count += 1
        return count
    
    return inc

fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0))) # Notice 0 has the same memory address than count is pointing.

fn()
print(fn.__closure__) # Notice memory address has changed, due to an integer is a singletone object.
print(hex(id(1)))

#%%

def outer():
    count = 0
    
    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count
    
    return inc1, inc2

fn1, fn2 = outer()
print(fn1.__code__.co_freevars, fn2.__code__.co_freevars)
print(fn1.__closure__, fn2.__closure__)
res = fn1()
print(res)
print("--------------------------------")
print(fn1.__closure__, fn2.__closure__) # Notice the memory address of the object has changed.
res = fn2()
print(res)
print("--------------------------------")
print(fn1.__closure__, fn2.__closure__) # Notice the memory address of the object has changed again.

#%%

def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(2)
print(square.__closure__)
print(hex(id(2)))

cube = pow(3)
print(cube.__closure__) # Notice the cell address is different of square
print(hex(id(3)))

#%%

def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
# The cells between add_1, add_2 and add_3 are different:
print(add_1.__closure__, add_2.__closure__, add_3.__closure__)

#%%
# We can think in creating a loop for doing the code above:

adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

print(adders) # Notice this is not a closure
print(adders[0].__closure__)

res = adders[0](10)
print(res) # And it does not as expected

#%%

def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x + n)
    return adders

adders = create_adders()
print(adders)
print(adders[0].__closure__) # Now it is a closure

res = adders[0](10) # Continue not working as expected
print(res)
print(adders[0].__closure__) # Notice all closures point to the same memory address
print(adders[1].__closure__)
print(adders[2].__closure__)

#%%
# For fixing the issue above you can not use closures, you need the n could be
# found when the function is created, not when is called:

def create_adders():
    adders = []
    for n in range(1, 4):
        # Using a default y=n closures are not created. 
        # Default is evaluated at creation time.
        adders.append(lambda x, y=n: x + y)
    return adders

adders = create_adders()
print(adders)
print(adders[0].__closure__) # adders] has not closures
print(adders[0].__code__.co_freevars) # Notice does not exist free variables

res = adders[0](10)
print(res)
res = adders[1](10)
print(res) # Now is working as expected.

#%%