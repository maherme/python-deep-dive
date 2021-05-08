#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 01:10:05 2021

@author: maherme
"""

import sys

print('===========================================')

print('Running main.py - module name: {0}'.format(__name__))

import module1 # Notice importing module1 is running the module.

print(module1)

module1.pprint_dict('main.globals', globals())

print(sys.path) # The module1 is found because the path of example1 is here.

print('Importing module1 again...')
import module1 # Notice nothing happens, because module1 is in the cache.

print('===========================================')