"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm undefined for non-positive values (a <= 0 or b <= 0).")
    return math.log(b, a)

def exp(a, b):
    return a ** b