#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 13:17:08 2021

@author: maherme
"""
#%%

import decimal
from decimal import Decimal

print(decimal.getcontext())

# We can change values in the context
decimal.getcontext().prec = 6
print(decimal.getcontext())

#%%
# You can also change the context in this way:

g_ctx = decimal.getcontext()
g_ctx.rounding = decimal.ROUND_HALF_UP # In this way you avoid misspelling
print(decimal.getcontext())

#%%
# Restore the original values:

g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN
print(decimal.getcontext())

#%%
# Notice the difference between the localcontext and the getcontext type:

print(type(decimal.localcontext()))
print(type(decimal.getcontext()))

#%%
# Notice the localcontext is the same than getcontext:

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(ctx)
    print(decimal.getcontext())
    print(id(ctx) == id(decimal.getcontext()))
    
#%%
# Notice the difference between context:

x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1))
    print(round(y, 1))
print(round(x, 1))
print(round(y, 1))

#%%