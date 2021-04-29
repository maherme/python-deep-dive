#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 15:46:48 2021

@author: maherme
"""
#%%

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result
    
    return inner

@logged
def func_1():
    pass

@logged
def func_2():
    pass

func_1()
func_2()

#%%
# We can use the decorator from DecoratorApplicationTiming.py:

def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    
    return inner

# We can decorate a function with two decorators:

@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

fact(3)

#%%
# We can specify two decorators in this other way:

def fact(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

fact = logged(timed(fact))
fact(6)

#%%
# Let's do an example for understanding what decorator runs first:

def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('Running dec_2')
        return fn()
    return inner

@dec_1
@dec_2
def my_func():
    print('Running my_func')

my_func()

#%%
# Notice my_func is called first now:

def dec_1(fn):
    def inner():
        result = fn()
        print('Running dec_1')
        return result
    return inner

def dec_2(fn):
    def inner():
        result = fn()
        print('Running dec_2')
        return result
    return inner

@dec_1
@dec_2
def my_func():
    print('Running my_func')

my_func()

#%%