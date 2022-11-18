# -*- coding: utf-8 -*-
"""
https://www.programiz.com/python-programming/examples/fibonacci-sequence
Recursive tree
recursive calls
o(n) time 
o(n) space 
"""

cache = {0: 0, 1: 1}

def fibonacci_of(n):
    if n in cache:  # Base case
        return cache[n]
    # Compute and cache the Fibonacci number
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
    return cache[n]

def foo(n):
    if n <= 1: 
        return foo(n-1)
    
def bar(n):
    if n <= 1: 
        return foo(n-2)
def dib(n):
    if n <= 1: 
        return [ dib(n-1), dib(n-1) ]
# a = [fibonacci_of(n) for n in range(15)]
# foo(5)
