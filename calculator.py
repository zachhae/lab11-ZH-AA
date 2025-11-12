"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        print("Number cannot be negative") # raise ValueError if a < 0

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise(ZeroDivisionError)
    else:
        b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    if b <= 0:
        raise(ValueError)
    else:
        math.log(b, a) # use math library + raise ValueError

def exp(a, b):
    return a ** b