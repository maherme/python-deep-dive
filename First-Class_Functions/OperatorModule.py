#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 20:27:45 2021

@author: maherme
"""
#%%

import operator

dir(operator) # You can see the attributes typing this in the command line

#%%

res = operator.add(1, 2)
print(res)
res = operator.mul(2, 3)
print(res)
res = operator.truediv(3, 2)
print(res)
res = operator.floordiv(13, 2)
print(res)

#%%

from functools import reduce

res = reduce(lambda x, y: x*y, [1, 2, 3, 4])
print(res)

res = reduce(operator.mul, [1, 2, 3, 4])
print(res)

#%%

res = operator.lt(10, 3)
print(res)

#%%

from operator import is_

res = is_('abc', 'def')
print(res)
res = is_('abc', 'abc')
print(res)

#%%

res = operator.truth([])
print(res)
res = operator.truth([1])
print(res)

#%%

my_list = [1, 2, 3, 4]
res = operator.getitem(my_list, 1)
print(res)
operator.setitem(my_list, 1, 100)
print(my_list)
operator.delitem(my_list, 3)
print(my_list)

#%%

f = operator.itemgetter(2)
print(type(f)) # f is a callable

my_list = [1, 2, 3, 4]
res = f(my_list)
print(res)

#%%

f = operator.itemgetter(2, 3)
my_list = [1, 2, 3, 4]
res = f(my_list)
print(res)
res = f('python')
print(res)

#%%

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    
    def test(self):
        print('test method running...')

obj = MyClass()

prop_a = operator.attrgetter('a') # Returns a callable.
res = prop_a(obj)
print(res)

my_var = 'b'
prop_b = operator.attrgetter(my_var)
res = prop_b(obj)
print(res)
my_var = 'c'
res = prop_b(obj) # Beware of prob_b continues looking for b.
print(res)

a, b, test = operator.attrgetter('a', 'b', 'test')(obj)
print(a, b, test)
test() # This calls the method.

#%%

f = lambda x: x.a
print(f(obj))

f = lambda x: (x[2], x[3])
x = [1, 2, 3, 4]
print(f(x))

#%%
# Let's look at sorting:

l = [5-10j, 3+3j, 2-100j]
res = sorted(l, key=lambda x: x.real)
print(res)

res = sorted(l, key=operator.attrgetter('real')) # You don't need to use lambda
print(res)

#%%

l = [(2, 3, 4), (1, 3, 5), (6,), (4, 100)]
res = sorted(l, key=lambda x: x[0])
print(res)

res = sorted(l, key=operator.itemgetter(0))
print(res)

#%%

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def test(self, c):
        print(self.a, self.b, c)

obj = MyClass()

print(obj.a, obj.b)
obj.test(100)

operator.methodcaller('test', 100)(obj) # You can call a method in this way

#%%

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def test(self, c, d, *, e):
        print(self.a, self.b, c, d, e)

obj = MyClass()

obj.test(100, 200, e=300)
operator.methodcaller('test', 100, 200, e=300)(obj)

f = operator.attrgetter('test')
f(obj)(100, 200, e=100)