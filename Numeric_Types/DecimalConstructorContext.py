#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:51:45 2021

@author: maherme
"""
#%%

import decimal
from decimal import Decimal

# You can create a decimal in different ways:
print(Decimal(10))
print(Decimal(-10))
print(Decimal('10.1'))
print(Decimal('-3.1415'))

#%%

# You can also use a tuple:
t = (0, (3, 1, 4, 1, 5), -4)
print(Decimal(t))
# Or directly using:
print(Decimal((0, (3, 1, 4, 1, 5), -4)))
print(Decimal((1, (3, 1, 4, 1, 5), -4)))
print(Decimal((1, (3, 1, 4, 1, 5), -3)))

#%%
# Notice what happens if you pass a non finite number to decimal:
    
print(Decimal(0.1)) # Here we are passing a float which is not finite.
print(Decimal('0.1'))
print(Decimal(0.1) == Decimal('0.1'))

#%%
# Notice the precision does not affect the constructor:

decimal.getcontext().prec = 6
a = Decimal('0.123456789')
print(a)

#%%

decimal.getcontext().prec = 2
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a, b)

# Notice the difference due to the precision is applied to the operation:
print(0.12345 + 0.12345)
print(a + b)

#%%
# Let's see how the localcontext and the globalcontext are independent:

decimal.getcontext().prec = 6
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c wihtin local context: {0}'.format(c))
print('c wihtin local context: {0}'.format(c)) # c is 0.25 whatever context

#%%