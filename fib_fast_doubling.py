# Fast doubling Fibonacci algorithm
# 
# Copyright (c) 2015 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# http://www.nayuki.io/page/fast-fibonacci-algorithms

# this is not my code - just testing it out!

import sys

# (Public) Returns F(n).
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

n = sys.argv[1]
fibonacci(n)