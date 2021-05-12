#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:06:42 2021

@author: maherme
"""
#%%
# Since Python 3.6 the order in which keyword arguments are collected into
# **kwargs is now maintained.

from sys import version_info
print(version_info)

#%%

def func(**kwargs):
    for item in kwargs.items():
        print(item)

func(b=100, a=200, y='hello', p='python')

#%%

from collections import namedtuple

def defaulted_namedtuple(class_name, **fields):
    Struct = namedtuple('Struct', fields.keys())
    Struct.__new__.__defaults__ = tuple(fields.values())
    return Struct

Vector2D = defaulted_namedtuple('Vector2D',
                              x1=None, y1=None,
                              x2=None, y2=None,
                              origin_x=0, origin_y=0)

print(Vector2D)
print(Vector2D._fields)

v1 = Vector2D(10, 10, 20, 20)
print(v1)

#%%