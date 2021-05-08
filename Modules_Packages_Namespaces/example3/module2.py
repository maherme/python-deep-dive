#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:55:10 2021

@author: maherme
"""

print('Running module2.py')

import module1

def hello():
    print('module2 says Hello!\nand...')
    module1.hello()