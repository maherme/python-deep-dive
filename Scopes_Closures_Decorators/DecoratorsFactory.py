#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 18:33:09 2021

@author: maherme
"""
#%%
# Let's do a time decorator for applying to fibonacci function:

def timed(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end -start
        print('Run time: {0:.6f}s'.format(elapsed))
        return result
    
    return inner

def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib)
fib(30)

#%%
# We can calculate a mean of the time, maybe 10 times:

def timed(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end -start)
        avg_run_time = total_elapsed / 10
        print('Avg run time: {0:.6f}s'.format(avg_run_time))
        return result
    
    return inner

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib)
fib(28)

#%%
# Let's try to parametrize tne number of loops in the for:

def timed(fn, reps):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end -start)
        avg_run_time = total_elapsed / reps
        print('Avg run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
        return result
    
    return inner

def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib, 5)
fib(28)

#%%
# Notice the following will fail:

@timed(5)
def fib(n):
    return calc_fib_recurse(n)

#%%
# Let's fix that:

def dec(fn):
    print("running dec")
    
    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)
    
    return inner

@dec
def my_func():
    print("running my_func")

#%%
# Or:

def my_func():
    print("running my_func")
    
my_func = dec(my_func)
print("-----------------")
my_func()

#%%
# Let's create a decorator factory:

def dec_factory():
    print("running dec_factory")
    
    def dec(fn):
        print("running dec")
        
        def inner(*args, **kwargs):
            print("running inner")
            return fn(*args, **kwargs)
        
        return inner
    return dec

dec = dec_factory()

@dec
def my_func():
    print("running my_func")

print("----------------")
my_func()

#%%
# Similar way to do the above:

@dec_factory()
def my_func():
    print("running my_func")

#%%
# Or:

def my_func():
    print("running my_func")

my_func = dec_factory()(my_func)

#%%
# We can use parameters in dec_factory:

def dec_factory(a, b):
    print("running dec_factory")
    
    def dec(fn):
        print("running dec")
        
        def inner(*args, **kwargs):
            print("running inner")
            print("a={0}, b={1}".format(a, b))
            return fn(*args, **kwargs)
        
        return inner
    return dec

dec = dec_factory(10, 20)

@dec
def my_func():
    print("running my_func")

print("------------------")
my_func()

#%%

@dec_factory(100, 200)
def my_func():
    print("running my_func")

print("------------------")
my_func()

#%%

my_func = dec_factory(150, 250)(my_func)
print("------------------")
my_func()

#%%
# Let's modify now our timed decorator:

def dec_factory(reps):
    def timed(fn):
        from time import perf_counter
        
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end -start)
            avg_run_time = total_elapsed / reps
            print('Avg run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result    
        return inner
    return timed

@dec_factory(5)
def fib(n):
    return calc_fib_recurse(n)

fib(28)

#%%

@dec_factory(15)
def fib(n):
    return calc_fib_recurse(n)

fib(28)

#%%
# Let's change the name of dec_factory:

def timed(reps):
    def dec(fn):
        from time import perf_counter
        
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end -start)
            avg_run_time = total_elapsed / reps
            print('Avg run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result    
        return inner
    return dec

@timed(15)
def fib(n):
    return calc_fib_recurse(n)

fib(28)

#%%