#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:53:47 2021

@author: maherme
"""
#%%
# You can define a complex number in different ways:
    
a = complex(1, 2)
print(a)
b = 1 + 2j
print(b)
print(a == b)

print(a.real, type(a.real)) # Notice real and imag part are float
print(a.imag, type(a.imag))

#%%
# You can use math operations:

print(a.conjugate())
print(a + b)
print(a * b)
print(a/b)
print(a ** 2)

#%%
# Operator // and % does not work:

a % 2 # All this operations will fail
a // 2
divmod(a, b)

#%%
# Notice we will have the same problems with precison due to the float:

a = 0.1j
print(format(a.imag, '.25f'))

print(a + a + a == 0.3j)
print(format((a+a+a).imag, '.25f'))
print(format((0.3j).imag, '.25f'))

#%%
# Exist a library cmath for complex numbers:

import cmath
import math

print(cmath.pi)
print(type(cmath.pi)) # Some items as pi will kept the same type

#%%
# There are functions than only works with imag number

a = 1 + 2j
print(cmath.sqrt(a))
math.sqrt(a) # This will not work

#%%
# cmath has some specific functions as phase or changing coordenate system

a = 1 + 1j

print(cmath.phase(a))
print(cmath.pi/4)

# rect function pass from polar to rectangular coord.
print(cmath.rect(math.sqrt(2), math.pi/4))

#%%
# Let's see e^(j*pi)+1 = 0

RHS = cmath.exp(cmath.pi * 1j) + 1
print(RHS)

print(cmath.isclose(RHS, 0)) # Notice this is false due to default tolerances
print(cmath.isclose(RHS, 0, abs_tol=0.0001))

#%%