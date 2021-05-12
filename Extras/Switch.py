#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:59:55 2021

@author: maherme
"""
#%%
# Let's emulate a switch case in python:

def dow_switch_fn(dow):
    if dow == 1:
        fn = lambda: print('Monday')
    elif dow == 2:
        fn = lambda: print('Tuesday')
    elif dow == 3:
        fn = lambda: print('Wednesday')
    elif dow == 4:
        fn = lambda: print('Thursday')
    elif dow == 5:
        fn = lambda: print('Friday')
    elif dow == 6:
        fn = lambda: print('Saturday')
    elif dow == 7:
        fn = lambda: print('Sunday')
    else:
        fn = lambda: print('Invalid day of week')
    
    return fn()

dow_switch_fn(1)
dow_switch_fn(100)

#%%
# Other way to do the above:

def dow_switch_dict(dow):
    dow_dict = {
        1: lambda: print('Monday'),
        2: lambda: print('Tuesday'),
        3: lambda: print('Wednesday'),
        4: lambda: print('Thursday'),
        5: lambda: print('Friday'),
        6: lambda: print('Saturday'),
        7: lambda: print('Sunday'),
        'default': lambda: print('Invalid day of week')
    }
    
    return dow_dict.get(dow, dow_dict['default'])()

dow_switch_dict(1)
dow_switch_dict(100)

#%%
# A third way to implement a switch case, based on singledispatcher:

def switcher(fn):
    registry = dict()
    registry['default'] = fn
    
    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn
        return inner
    
    def decorator(case):
        fn = registry.get(case, registry['default'])
        return fn()
    
    decorator.register = register
    return decorator

@switcher
def dow():
    return 'Invalid day of week'

@dow.register(1)
def dow_1():
    return 'Monday'
# We can do the above in shorter way:
dow.register(2)(lambda: 'Tuesday')
dow.register(3)(lambda: 'Wednesday')
dow.register(4)(lambda: 'Thursday')
dow.register(5)(lambda: 'Friday')
dow.register(6)(lambda: 'Saturday')
dow.register(7)(lambda: 'Sunday')

print(dow(1))
print(dow(100))

#%%