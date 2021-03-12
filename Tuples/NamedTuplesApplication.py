#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:19:31 2021

@author: maherme
"""
#%%

from random import randint, random
from collections import namedtuple

def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha

color = random_color()
print(color)
red, green, blue, alpha = color
print(red, green, blue, alpha)

#%%

Color = namedtuple('Color', 'red green blue alpha')

def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)

color = random_color()
print(color)
print(color.red, color.alpha)

#%%
