#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:33:42 2021

@author: maherme
"""
#%%
# X or Y: if X is truthy, returns X, otherwise evaluates Y and returns it

print('a' or (1, 2))
print('' or (1, 2))
print(1 or 1/0)
print(0 or 1/0) # This will fail because 1/0 is evaluated

#%%
# An example of using assignment and default values:

s1 = None
s2 = ''
s3 = 'abc'

s1 = s1 or 'n/a'
s2 = s2 or 'n/a'
s3 = s3 or 'n/a'

print(s1, s2, s3)

#%%
# X and Y: if X is falsy, returns X, otherwise evaluates Y and returns it

print(None and 100)
print([] and [0])

#%%
# a/b in general, but return 0 when b is zero

a = 2
b = 4

if b == 0:
    print(0)
else:
    print(a/b)

#%%
# Another way to write the code above is:

a = 2
b = 0
print(b and a/b)

#%%
# Let's see other case:

# In this case s1[0] and s2[0] will fail
s1 = None
s2 = ''
s3 = 'abc'

# s[0] will not fail in whatever case now:
print((s1 and s1[0]) or 'n/a')
print((s2 and s2[0]) or 'n/a')
print((s3 and s3[0]) or 'n/a')

#%%