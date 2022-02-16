import sys
import mpmath
import sympy

from sympy import *

x_values = tuple(range(3, 1000, 3))

y_values = tuple(range(5, 1000, 5))

alpha = x_values + y_values

final_set= set(alpha)

beta=sum(final_set)

print(beta)

#So, this was a little annoying-- I couldn't figure out how to eliminate duplicates; Apparently in python, if you define a "list"
#or a "range" then you have limited capacity for modification; "tuples" work better (see lines 7,9, where originally I used just range, then list(range), etc)
#At 11, the issue was just the duplicates -- the "Set()" option allows for the integration of values, deleting duplicates; 
#after they're deleted, it's just a matter of finding the sum.

#Some other options from the website: 

print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 ==0]))