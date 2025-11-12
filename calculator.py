"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    try:
        return math.sqrt(a)
    except Exception as e:
        print(f"Error in square_root: {e}")
        return

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print(f"Error in hypotenuse: {e}")
        return
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