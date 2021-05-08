# helpers

from .calculator import Calc

# You can do this but it is not a good practice, here you should put code only
# related with building or configuring the packet
def say_hello(name):
    return f'Hello {name}'

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)