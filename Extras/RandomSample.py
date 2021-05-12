#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:52:35 2021

@author: maherme
"""
#%%
# sample does not use replacement

import random

l = list(range(10))
print(random.choices(l, k=5)) # Here you have the risk to have repetitions.
print(random.sample(l, k=5)) # Here you have not repetitons.

#%%
# Let's see an example using a deck simulator:

suits = 'C', 'D', 'H', 'S'
ranks = tuple(range(2, 11)) + tuple('JQKA')

#%%

deck = []
for suit in suits:
    for rank in ranks:
        deck.append(str(rank) + suit)

print(deck)

#%%
# Or using list comprehension:

deck = [str(rank) + suit for suit in suits for rank in ranks]
print(deck)

#%%
# Notice using sample you don't get repetitions:

from collections import Counter

Counter(random.choices(deck, k=40))
Counter(random.sample(deck, k=52))

#%%