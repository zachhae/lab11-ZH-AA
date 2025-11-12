"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

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

def exp(a, b): a ** b