#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 20:40:10 2021

@author: maherme
"""
#%%
# Let's create a decorator:

def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        
        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__, args_str, elapsed))
        
        return result
    
    return inner

#%%
# Let's do a functon to calculate Fibonacci using: recursion, loop and reduce:

def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

@timed
def fib_recursive(n): # We create this wrap function to avoid call decorator recursively
    return calc_recursive_fib(n)

fib_recursive(35)

#%%
# Let's implement Fibonacci using a loop:

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

fib_loop(35)

#%%
# Let's do it using reduce:
#
# n = 1
# (1, 0) --> (1, 1) retult t[0] = 1
#
# n = 2
# (1, 0) --> (1, 1) --> (2, 1) result t[0] = 2
#
# n = 3
# (1, 0) --> (1, 1) --> (2, 1) --> (3, 2) result t[0] = 3
#
# n = 4
# (1, 0) --> (1, 1) --> (2, 1) --> (3, 2) --> (5, 3) result t[0] = 5
#
# previous value = (a, b)
# new value = (a+b, a)

from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)

    return fib_n[0]

fib_reduce(35)

#%%
# For timer purpose we can run the function more than once and return the mean
# value of time:

def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0
        
        for i in range(10):
            print('Running iteration {0}...'.format(i))
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            elapsed_total += elapsed
            elapsed_count += 1
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        
        elapsed_avg = elapsed_total / elapsed_count
        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__, args_str, elapsed_avg))
        
        return result
    
    return inner

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)

    return fib_n[0]

fib_reduce(100)

#%%
# If you don't want to have 10 hardcoded:
    
def timed(fn, count):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0
        
        for i in range(count):
            print('Running iteration {0}...'.format(i))
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            elapsed_total += elapsed
            elapsed_count += 1
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        
        elapsed_avg = elapsed_total / elapsed_count
        print('{0}({1}) took {2:.6f}s to run'.format(fn.__name__, args_str, elapsed_avg))
        
        return result
    
    return inner

def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)

    return fib_n[0]

fib_reduce = timed(fib_reduce, 15) # Notice you can not use @timed if count is passing as parameter.

fib_reduce(100)

#%%