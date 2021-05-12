#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:46:06 2021

@author: maherme
"""
#%%

def validate(a=None):
    if a is not None:
        print('argument was provided')
    else:
        print('argument was NOT provided')

validate()
validate(10)
validate(None) # We can not differentiate this to the first call validate().

#%%
# Let's try to solve the above:

_sentinel = object()

def validate(a=_sentinel):
    if a is not _sentinel:
        print('argument was provided')
    else:
        print('argument was NOT provided')

validate()
validate(10)
validate(None)

#%%
# A better way:

def validate(a=object()):
    default_a = validate.__defaults__[0]
    if a is not default_a:
        print('argument was provided')
    else:
        print('argument was NOT provided')

validate()
validate(10)
validate(None)

#%%
# If you want to use the check for more arguments:

def validate(a=object(), b=object(), *, kw=object()):
    default_a = validate.__defaults__[0]
    default_b = validate.__defaults__[1]
    default_kw = validate.__kwdefaults__['kw']
    
    if a is not default_a:
        print('argument a was provided')
    else:
        print('argument a was NOT provided')

    if b is not default_b:
        print('argument b was provided')
    else:
        print('argument b was NOT provided')

    if kw is not default_kw:
        print('argument kw was provided')
    else:
        print('argument kw was NOT provided')

validate(100, 200, kw=None)
validate(200)

#%%