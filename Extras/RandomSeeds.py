#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:35:44 2021

@author: maherme
"""
#%%

import random

for _ in range(10):
    print(random.randint(10, 20), random.random())

#%%
# Every time you reset the seed the sequence will start with the same values:

random.seed(0)

for _ in range(10):
    print(random.randint(10, 20), random.random())

print("----------------------")
random.seed(0)

for _ in range(10):
    print(random.randint(10, 20), random.random())

#%%
# random has other interested methods like shuffle or gauss:

def generate_random_stuff(seed=None):
    random.seed(seed)
    results = []
    
    for _ in range(5):
        results.append(random.randint(0, 5))
    
    characters = list('abc')
    random.shuffle(characters)
    results.append(characters)
    
    for _ in range(5):
        results.append(random.gauss(0, 1))
    
    return results

#%%

generate_random_stuff()
generate_random_stuff(0)
# We get the same result than above if we use the same seed
generate_random_stuff(0)
generate_random_stuff(25)
# We get the same result than above if we use the same seed
generate_random_stuff(25)

#%%
# How to test the above?. We can do a frequency analysis:

def freq_analysis(lst):
    return {k: lst.count(k) for k in set(lst)}

lst = [random.randint(0, 10) for _ in range(100)]
print(lst)
set(lst)

freq_analysis(lst) # You can see frequency is not uniform

#%%
# We can increase the number:

d = freq_analysis([random.randint(0, 10) for _ in range(1_000_000)])
total = sum(d.values()) # total has to match with 1 million.
{k: v/total * 100 for k, v in d.items()}

#%%
# The functionality above is implemented in Counter class:

from collections import Counter

Counter([random.randint(10, 20) for _ in range(100_000)])

#%%