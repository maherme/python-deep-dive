#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:07:29 2021

@author: maherme
"""
#%%

class Averager:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

a = Averager()
ret = a.add(10)
print(ret)
ret = a.add(20)
print(ret)
ret = a.add(30)
print(ret)

#%%
# We can do the code above using closures:

def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager()
ret = a(10)
print(ret)
ret = a(20)
print(ret)
ret = a(30)
print(ret)

b = averager()
ret = b(10)
print(ret)

print(a.__closure__)
print(b.__closure__)

#%%
# Let's optimize the code above:

def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total / count
    return add

a = averager()
print(a.__closure__)
print(a.__code__.co_freevars)

ret = a(10)
print(ret)
ret = a(20)
print(ret)

#%%
# You can do the same with class:

class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0
        
    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count

#%%
# Let's move to other example:

from time import perf_counter

class Timer:
    def __init__(self):
        self.start = perf_counter()
        
    def poll(self):
        return perf_counter() - self.start

t1 = Timer()

#%%
ret = t1.poll()
print(ret)

#%%

class Timer:
    def __init__(self):
        self.start = perf_counter()
        
    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()

#%%
# Now calling Timer we call the previous poll method:

ret = t1()
print(ret)

#%%
# Using closures:

def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()

#%%

ret = t2()
print(ret)

#%%
# Let's do other example:

def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter1 = counter()
ret = counter1()
print(ret)
ret = counter1()
print(ret)

#%%

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)
res = counter_add(10, 20)
print(res)
counter_mult = counter(mult)
res = counter_mult(2, 5)
print(res)

#%%

counters = dict()

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

counter_add = counter(add)
counter_mult = counter(mult)

counter_add(10, 20)
counter_add(20, 30)
print(counters)
counter_mult(2, 5)
print(counters)

#%%
# We can pass counters as parameter:

def counter(fn, counters):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

c = dict()
counted_add = counter(add, c)
counted_mult = counter(mult, c)

print(counters)

counted_add(10, 20)
counted_mult(2, 5)
counted_mult(3, 6)

print(counters)
print(c)

#%%
# Other example:

def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

ret = fact(3)
print(ret)

counted_fact = counter(fact, c)
ret = counted_fact(5)
print(ret)
print(c)

#%%

fact = counter(fact, c) # Notice we are modifying the function fact adding some extra bits.
print(fact.__closure__)
ret = fact(3)
print(ret)
ret = fact(5)
print(ret)
print(c)
add = counter(add, c) # Same with add.
ret = add(10, 20)
print(ret)
print(c)

#%%