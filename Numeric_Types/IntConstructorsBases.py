#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:11:49 2021

@author: maherme
"""
#%%
# For documentation about class int you can watch help(int)

# It is not neede to pass a integer number to the constructor of the int class
print(int(10.5))
print(int(10.99999))
print(int(True))
print(int(False))

import fractions

a = fractions.Fraction(22, 7)
print(a)
print(float(a))
print(int(a))

#%%
# The default base is 10 in the constructor:

print(int("12345"))
print(int("101", 2))
print(int("FF", 16))

#%%
# We can use built-in representation:

print(bin(10))
print(bin(5))
print(oct(10))
print(hex(255))

a = int('101', 2)
b = 0b101
print(a)
print(b)

#%%
# Let's see custom base conversion:
    
def from_base10(n, b):
    if n < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return[0]
    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits

print(from_base10(10, 2))
print(from_base10(255, 16))

#%%
# Let's do the encoding:

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    # encoding = ''
    # for d in digits:
    #     encoding += digit_map[d]
    # return encoding
    return ''.join([digit_map[d] for d in digits])

print(encode([15, 15], '0123456789ABCDEF'))

#%%
# We can combine the two functions above:

def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    sign = -1 if number < 0 else 1
    number *= sign
    
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

e = rebase_from10(314, 2)
print('***** number 314 base 2 *****')
print(e)
print(int(e, base=2))

e = rebase_from10(-314, 2)
print('***** number -314 base 2 *****')
print(e)
print(int(e, base=2))

e = rebase_from10(3451, 16)
print('***** number 3451 base 16 *****')
print(e)
print(int(e, base=16))

e = rebase_from10(-3451, 16)
print('***** number -3451 base 16 *****')
print(e)
print(int(e, base=16))

#%%