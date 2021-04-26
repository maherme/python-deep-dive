#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 23:15:17 2021

@author: maherme
"""
#%%

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

result = fact(3)
print(result)
result = fact(4)
print(result)

results = map(fact, range(6))
print(results)

for x in results: # map does not calculate the elements, these are calculated when are requested.
    print(x)

#%%

results = list(map(fact, range(6))) # This calculates the elements
print(results)

#%%

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]

results = list(map(lambda x, y: x+y, l1, l2))
print(results) # When one of the elements will be exhausted, the map finishes.

#%%

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = 100, 200, 300, 400

results = list(map(lambda x, y, z: x+y+z, l1, l2, l3))
print(results)

#%%

results = map(lambda x, y: x+y, l1, l2, l3)
print(results) # Notice this does not fail

#%%

for x in results: # It fails here, because map calculates the element when they are requested.
    print(x)

#%%

x = range(25)
print(x) # Notice range is not calculated.

for i in x: # Now is range calculated. When is requested.
    print(i)

#%%

for i in x: # Notice you can reuse.
    print(i)

#%%

result = list(filter(lambda x: x % 3 == 0, range(25)))
print(result)

#%%

result = list(filter(None, [1, 0, 4, 'a', '', None, True, False]))
print(result)

#%%

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = 'python'

results = zip(l1, l2, l3) # This is not a list.

for x in results:
    print(x)

#%%

for x in results: # Notice you can not reuse, because is not a list
    print(x)

#%%

results = list(zip(l1, l2, l3))

for x in results:
    print(x)

#%%

for x in results: # Now you can reuse
    print(x)
    
#%%
# You can use zip for indexing:
    
results = list(zip(range(10000), 'python'))
print(results)

#%%

l = range(10)
print(l)
print(list(l))
results = list(map(fact, l))
print(results)
results = [fact(n) for n in range(10)]
print(results)

#%%

results = (fact(n) for n in range(10)) # If you use () instead [] you create a generator.
print(results)

for x in results:
    print(x)

#%%

for x in results: # The iteration has exhausted results.
    print(x)

#%%

results = list((fact(n) for n in range(10))) # If you use a list you can reuse:
print(results)

for x in results:
    print(x)

#%%

for x in results: # The iteration has exhausted results.
    print(x)

#%%

l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]

results = list(map(lambda x, y: x+y, l1, l2))
print(results)

results = [x+y for x, y in zip(l1, l2)] # Notice this is the same as above
print(results)

# For getting only even numbers:
results = list(filter(lambda x: x%2==0, map(lambda x, y: x+y, l1, l2)))
print(results)

# Other way to do it
results = [x+y for x, y in zip(l1, l2) if (x+y)%2 == 0]
print(results)

#%%

# You can do a generator:
results = (x+y for x, y in zip(l1, l2) if (x+y)%2 == 0)
print(results)
print(list(results))

#%%