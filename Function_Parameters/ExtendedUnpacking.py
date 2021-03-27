#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:48:42 2021

@author: maherme
"""
#%%
# Slicing:

l =  [1, 2, 3, 4, 5, 6]

a = l[0]
b = l[1:]
print(a)
print(b)

a, b = l[0], l[1:]
print(a, b)

#%%
# Extended unpacking:

a, *b = l
print(a, b)

#%%
# This does not work with iterables non indexables:

s = {1, 2, 3}
a = s[0]
b = s[1:]

#%%
# Notice in these cases the unpacking is in a list and not in a string or a
# tuple:

s = 'python'

a, *b = s
print(a, b)

t = ('a', 'b', 'c')

a, *b = t
print(a, b)

#%%

s = 'python'

a, b, *c = s
print(a, b, c)

a, b, *c, d = s
print(a, b, c, d)

a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a, b, c, d) # Notice c is not a list, you have to unpack c if you want a list

*c, = c
print(c)

#%%

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
s = 'abc'
l = [*l1, *s]
print(l)

l1 = [1, 2, 3]
s1 = {'x', 'y', 'z'}
l = [*l1, *s1]
print(l) # Remember, set does not keep the order

s1 = 'abc'
s2 = 'cde'
l = [*s1, *s2]
print(l)

l = {*s1, *s2}
print(l) # Notice in a set the repeated elements are deleted

#%%
# Take into account unpack set or unordered data types could not be useful:

s = {10, -99, 3, 'd'}

for c in s:
    print(c)

a, b, c, d = s
print(a, b, c, d)

a, b, *c = s # You don't know which data is stored in c
print(a, b, c)

#%%
# You can convert a set into a list unpacking:

*c, = s
print(c)

#%%

s1 = {1, 2, 3}
s2 = {3, 4, 5}

c = {*s1, *s2}
print(c)

# You can also use union method
c = s1.union(s2)
print(c)

#%%

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}

c = s1.union(s2).union(s3).union(s4)
print(c)

c = [*s1, *s2, *s3, *s4]
print(c)

c = {*s1, *s2, *s3, *s4}
print(c) # Unpacking into a set you avoid repeated elements

#%%
# You can do the same with dictionaries:

d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key4': 4}

d = {*d1, *d2}
print(d) # Notice you only unpack the keys

d = {**d1, **d2}
print(d) # This is the right way if you want to unpack keys and values

#%%
# Nested unpacking:

a, b, (c, d) = [1, 2, 'XY']
print(a, b, c, d)

a, b, (c, d, *e) = [1, 2, 'python']
print(a, b, c, d, e)

#%%

l = [1, 2, 3, 4, 'python']
a, *b, (c, d, *e) = l
print(a, b, c, d, e)

# Let's do the same using slicing:
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)

#%%