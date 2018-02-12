#!/usr/bin/env python3
"""Introduction to Python"""

should_print = True
num1 = 2
num2 = 3.
num3 = 1/4 # or 1/4. in Python 2
hello = 'world'
another = "string"
some_primes = [2, 3, 5, 7, 3, 7]
xyz_coordinates = (3, 0, -1)
prime_set = set(some_primes)
mapping = {
    'xyz': xyz_coordinates,
    'primes': prime_set,
    hello: 'world'
}

# If not loaded as a module...
if __name__ == '__main__':
    # If should_print == True and mapping is not empty...
    if should_print and mapping:
        print(mapping)
