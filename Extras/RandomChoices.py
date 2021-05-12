#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:11:02 2021

@author: maherme
"""
#%%

import random

l = [10, 20, 30, 40, 50]
random_index = random.randrange(len(l))
l[random_index]

#%%

l = list(range(1000))
randoms = []

for _ in range(5):
    randoms.append(l[random.randrange(len(l))])

print(randoms)

#%%
# A more pythonic way to do this:

randoms = []

for _ in range(5):
    randoms.append(random.choice(l))

print(randoms)

#%%
# We can do using list comprehension, this a better option:

randoms = [random.choice(l) for _ in range(5)]
print(randoms)

#%%
# Probably the best way:

randoms = random.choices(l, k=5)
print(randoms)

#%%
# You can specify the weight of the choices:

l = ['a', 'b', 'c']
for _ in range(10):
    print(random.choices(l, k=5))

print("-----------------------------------")

weights = [10, 1, 1]
l = ['a', 'b', 'c']
for _ in range(10):
    print(random.choices(l, k=5, weights=weights))

#%%

from collections import namedtuple

Freq = namedtuple('Freq', 'count freq')

def freq_counts(lst):
    total = len(lst)
    return {k: Freq(lst.count(k), 100 * lst.count(k) / total) for k in set(lst)}

print(freq_counts(random.choices(l, k=100_000)))

#%%

weights = [8, 1, 1]
print(freq_counts(random.choices(l, k=100_000, weights=weights)))

#%%

cum_weights = [7, 8, 10]
print(freq_counts(random.choices(l, k=100_000, cum_weights=cum_weights)))

#%%

from time import perf_counter

random.seed(0)

denoms = random.choices([0, 1], k=10_000_000)

start = perf_counter()
for d in denoms:
    if d == 0:
        continue
    else:
        10 / d
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denoms):0.15f}')

start = perf_counter()
for d in denoms:
    try:
        10 / d
    except ZeroDivisionError:
        pass
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denoms):0.15f}')

#%%

random.seed(0)
denoms = random.choices([0, 1], k=10_000_000, weights=[1, 9])

start = perf_counter()
for d in denoms:
    if d == 0:
        continue
    else:
        10 / d
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denoms):0.15f}')

start = perf_counter()
for d in denoms:
    try:
        10 / d
    except ZeroDivisionError:
        pass
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denoms):0.15f}')

#%%