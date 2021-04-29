#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:28:04 2021

@author: maherme
"""
#%%
# You can modify method of classes:

from fractions import Fraction

Fraction.speak = lambda self, message: 'Fraction says: {0}'.format(message)
f = Fraction(2, 3)
res = f.speak('This is a late parrot')
print(res)

#%%

Fraction.is_integral = lambda self: self.denominator == 1
f1 = Fraction(2, 3)
f2 = Fraction(64, 8)
res = f1.is_integral()
print(res)
res = f2.is_integral()
print(res)

#%%

def dec_speak(cls):
    cls.speak = lambda self, message: '{0} says: {1}'.format(self.__class__.__name__, message)
    return cls

Fraction = dec_speak(Fraction)
f1 = Fraction(2, 3)
res = f1.speak('hello')
print(res)

#%%

class Person:
    pass

Person = dec_speak(Person)
p = Person()
res = p.speak('this works!')
print(res)

#%%
# Let's create some debug decorator:

from datetime import datetime, timezone

def info(self):
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('Class: {0}'.format(self.__class__.__name__))
    results.append('id: {0}'.format(hex(id(self))))
    for k, v in vars(self).items(): # vars() is a built-in function that returns all the properties of an object.
        results.append('{0}: {1}'.format(k, v))
    return results

def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return 'Hello there!'

p = Person('John', 1939)
res = p.debug()
print(res)

#%%
# This decorator can be reused in other classes:

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property # Built-in decorator
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top_speed.')
        else:
            self._speed = new_speed

favorite = Automobile('Ford', 'Model T', 1908, 45)
res = favorite.debug()
print(res)
print("-------------------------------")
favorite.speed = 40
res = favorite.debug()
print(res)

#%%