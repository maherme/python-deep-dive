#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 00:06:12 2021

@author: maherme
"""
#%%

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#%%

r1 = Rectangle(10, 20)
print(r1.width)

r1.width = 100
print(r1.width)

#%%
# You can define method of a class:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
#%%

r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter())

#%%

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
#%%

r1 = Rectangle(10, 20)
str(r1)
r1.to_string()

#%%
# You can overwrite a method:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
#%%

r1 = Rectangle(10, 20)
str(r1)
r1

#%%
# You can also overwrite the representation method:
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
#%%

r1 = Rectangle(10, 20)
str(r1)
r1

#%%
# Equality:
    
r2 = Rectangle(10, 20)
r1 is not r2
r1 == r2

#%%
# r1 == r2 is false because r1 and r2 are different instances.
# You can solve this problem doing the following:
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
# You can also do: (self.width, self.height) == (other.width, other.height)

#%%

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

r1 is not r2
r1 == r2

#%%
# We can face this problem:
    
r1 == 100

#%%
# You can solve the problem in this way:
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False
        
#%%

r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)

r1 == r2
r1 == 100

#%%
# We can implement other comparison methods like "less than"

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
        
#%%

r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)

r1 < r2
r2 < r1
r2 > r1 # This works because Python flip the comparison

#%%
# Other problem of this class is you can access to attributes directly. We can
# also sove this:
    
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width
    
    def get_height(self):
        return self._height
    
    def set_height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive')
        else:
            self._height = height
    
    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
        
#%%
# You can not access directly to an attribute just now

r1 = Rectangle(10, 20)
r1.width

#%%
# Be careful with the following, you are creating a new property, this is
# allowed in Python and it is called "monkey patching":
    
r1.width = -100
r1._width

#%%

r1.get_width()
r1.get_height()
r1.set_width(-100)
r1.set_width(100)

#%%
# Due to "monkey patching" and because you or other developer can break the
# compatibility of the program, in Python there is a better way to implement
# a solution for a getter and setter method:

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive')
        else:
            self._height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other.width and self._height == other.height
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
        
#%%

r1 = Rectangle(10, 20)
r1.width
r1.height
r1.width = -100
r1.width = 100

#%%
# But we face with other problem using the init method:
    
r1 = Rectangle(-100, 20)

#%%
# To sove this we can use the internal width and height method of the class:
    
class Rectangle:
    def __init__(self, width, height):
        self.width = width    # We use internal method here, removing "_"
        self.height = height  # We use internal method here, removing "_"
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive')
        else:
            self._height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other.width and self._height == other.height
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

#%%
# But we face with other problem using the init method:
    
r1 = Rectangle(-100, 20)

#%%