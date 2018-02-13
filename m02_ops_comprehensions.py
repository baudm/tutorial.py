#!/usr/bin/env python3

# This expression returns a list
even_numbers = [2 * i for i in range(5)]

# While this one returns a generator
squares = (i**2 for i in range(1, 6))

print(even_numbers)
print(squares)
print(list(squares))
# Second invocation of generator should return an empty list. Why?
print(list(squares))
