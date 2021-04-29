#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 11:10:53 2021

@author: maherme
"""
#%%

from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(k, v)
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

#%%

print(html_str(""" this is
               a multi line string
               with special characters: 10 < 100"""))

#%%

print(html_int(255))

#%%

print(html_escape(3+10j))

#%%

from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(arg)

print(htmlize(100))
print("------------------")
print(htmlize("""Python
rocks! 
"""))
print("------------------")
print(htmlize([1, 2, 3]))
print("------------------")
print(htmlize(["""Python
rocks! 0 < 1
""", (10, 20, 30), 100])) # Notice some values have not been htmlized.

#%%
#Let's fix it:

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), htmlize(v))
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlize(["""Python
rocks! 0 < 1
""", (10, 20, 30), 100])) # Not it works.

#%%
# We face other problem, every time we create a new function, we need to
# increase the elif function htmlize:

def html_set(arg): # We create this new function
    return html_list(arg)

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    elif isinstance(arg, set): # We need to increase the htmlize function
        return html_set(arg)
    else:
        return html_escape(arg)

print(htmlize({1, 2, 3}))

#%%
# Let's try fo fix this:

def htmlize(arg):
    registry = {
        object: html_escape,
        int: html_int,
        float: html_real,
        Decimal: html_real,
        str: html_str,
        list: html_list,
        tuple: html_list,
        set: html_set,
        dict: html_dict
    }
    
    fn = registry.get(type(arg), registry[object])
    
    return fn(arg)

print(htmlize(100))
print("------------------")
print(htmlize([1, 2, 3]))

#%%
# Let's use a decorator, trying to do the above in a more general way avoiding
# these hardcoded variables in registry:

def singledispatch(fn):
    registry = {}
    registry[object] = fn # Here we add fn in a generic way
    
    def inner(arg):
        return registry[object](arg) # It looks the function in the registry
    
    return inner

@singledispatch
def htmlize(a):
    return escape(str(a)) 

print(htmlize('1 < 100'))

#%%
# Looking the code above can seem some weird, but let's expand the code a bit
# more:

def singledispatch(fn):
    registry = {}
    registry[object] = fn
    registry[int] = lambda a: '{0}(<i>{1}</i>)'.format(a, str(hex(a)))
    registry[str] = lambda s: escape(s).replace('\n', '<br/>\n')
    
    def inner(arg):
        # Now we look for the type of arg in registry,  we get the function associated 
        # and we call it with arg:
        return registry.get(type(arg), registry[object])(arg)
    
    return inner

@singledispatch
def htmlize(a):
    return escape(str(a))

print(htmlize('1 < 100'))
print(htmlize(100))

#%%
# Notice the code above uses hardcoded functions as lambdas, let's try to
# avoid that:

def singledispatch(fn):
    registry = {}
    registry[object] = fn

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def register(type_): #  This will be the decorator factory
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    return decorated

@singledispatch
def htmlize(a):
    return escape(str(a))

print(htmlize('1 < 100'))
print(htmlize(100)) # This is not htmlized because is not in the registry

#%%
# For fixing the code avobe we need to call register decorator:

def singledispatch(fn):
    registry = {}
    registry[object] = fn

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    decorated.register = register # Here we fix the problem.
    return decorated

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

print(htmlize(100))

@htmlize.register(list)
def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

#%%
# You can stack decorators:

@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlize([1, 2, 3]))
print("----------------")
print(htmlize((1, 2, 3)))

#%%
# We can add an attribute to watch the registry:

def singledispatch(fn):
    registry = {}
    registry[object] = fn

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    decorated.register = register
    decorated.registry = registry
    return decorated

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

print(htmlize.registry)

@htmlize.register(list)
def html_list(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print("\n")
print(htmlize.registry)

@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print("\n")
print(htmlize.registry)

#%%
# This is a better options, avoiding to give access to registry:

def singledispatch(fn):
    registry = {}
    registry[object] = fn

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner
    
    def dispatch(type_):
        return registry.get(type_, registry[object])
    
    decorated.register = register
    decorated.dispatch = dispatch
    return decorated

@singledispatch
def htmlize(a):
    return escape(str(a))

print(htmlize.dispatch(int)) # Prints default because any function was registered for int

@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

print(htmlize(100))

print(htmlize.dispatch(int)) # Now we have one function for int

#%%
# There is some issues again:

from numbers import Integral

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def html_integral_number(a):
    return '{0}(<i>{1}</i>)'.format(1, str(hex(a)))

print(isinstance(10, Integral))
print(htmlize(10)) # Notice this does not work, we are using type not isinstance

#%%

from collections.abc import Sequence

print(isinstance([1, 2, 3], Sequence))
print(isinstance((1, 2, 3), Sequence))

@htmlize.register(Sequence) # We can register a Sequence abstract type
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

res = type([1, 2, 3]) is Sequence
print(res) # Notice the type is not a Sequence

#%%
# Exists a decorator for doing the dispatcher above:

from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence

@singledispatch
def htmlize(a):
    return escape(str(a))

@htmlize.register(Integral)
def htmlize_integral_number(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

print(htmlize.dispatch(int))
print(htmlize.dispatch(bool))
print(htmlize(10))
print(htmlize(True))

#%%

@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))

#%%
# But there is a problem here:

print(isinstance('python', Sequence))

#%%

print(htmlize('python')) # This fails, but it is a Sequence ...

# This fails because 'python' is a Sequence, is also a string, but when we
# iterate in the "for item in l" loop, we are getting each character, which is
# also a string and a Sequence ...

#%%
# We can fix this creating a more specific function than a Sequence:

@htmlize.register(str)
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

print(htmlize('python'))

#%%
# Notice the name of the functios are labels, what Python manages are the
# memory addresses, so you can write a code like this:

@htmlize.register(Integral)
def _(a):
    return '{0}(<i>{1}</i>)'.format(a, str(hex(a)))

@htmlize.register(Sequence)
def _(l):
    items = ('<li>{0}</li>'.format(htmlize(item))
             for item in l
            )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(str)
def _(s):
    return html_escape(s).replace('\n', '<br/>\n')

print(htmlize.registry)
print("-----------------")
print(_) # This is the last _ we have defined.
print("-----------------")
# But we can get access all the others _ functios defined above:
print(htmlize.dispatch(Integral))
print(id(htmlize.dispatch(Integral)))
print(htmlize.dispatch(str))
print(id(htmlize.dispatch(str)))
print(htmlize.dispatch(Sequence))
print(id(htmlize.dispatch(Sequence)))
print("-----------------")
print(id(_)) # Notice this memory address is the str because is the last function defined.

#%%